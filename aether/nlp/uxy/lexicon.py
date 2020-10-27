from __future__ import annotations

from typing import Optional, Union, Dict

from omnilingual import LanguageCode
from omnilingual.features import Clusivity, Gender, Number, Person
from omnilingual.features.uxy import XianMood

from aether.nlp.lexicon import Lexicon, Word, GrammaticalPattern
from aether.ontology.base import Entity, IsA
from aether.ontology.bdi import Need
from aether.ontology.family import Son
from aether.ontology.politics.state import MemberOfState
from aether.ontology.occupation.politics import Diplomat
from aether.ontology.occupation.education import Student
from aether.ontology.special import Id
from aether.ontology.misc import Also, Equivalent
from aether.ontology.movement.general import Travel
from aether.ontology.worlds.starcitizen.empires import UnitedEmpireOfEarth

lexicon = Lexicon()


class XianPronoun(Word):
    first_plural: Dict[XianMood, Dict[Clusivity, str]] = {
        XianMood.Neutral: {Clusivity.In: "yāng", Clusivity.Ex: "yuē"}
    }

    pronouns: Dict[
        XianMood, Dict[Person, Dict[Number, Dict[Optional[Gender], str]]],
    ] = {
        XianMood.Neutral: {
            Person.First: {Number.Sing: {None: "no’a"}},
            Person.Second: {Number.Sing: {None: "lē"}, Number.Plur: {None: "sē’a"},},
            Person.Third: {
                Number.Sing: {
                    Gender.Masc: "thlan",
                    Gender.Fem: "thlan",
                    Gender.Neut: "ku",
                },
                Number.Plur: {
                    Gender.Masc: "se’lan",
                    Gender.Fem: "se’lan",
                    Gender.Neut: "kum",
                },
            },
        }
    }

    def __init__(
        self,
        person: Person,
        number: Number,
        gender: Optional[Gender] = None,
        clusivity: Optional[Clusivity] = None,
        mood: XianMood = XianMood.Neutral,
    ):
        self.person = person
        self.number = number
        self.gender = gender
        self.clusivity = clusivity

        self.mood = mood

    @property
    def word(self) -> str:
        if (
            self.person is Person.First
            and self.number is Number.Plur
            and self.clusivity is not None
        ):
            return self.first_plural[self.mood][self.clusivity]
        else:
            return self.pronouns[self.mood][self.person][self.number][self.gender]


class LoIsA(GrammaticalPattern):
    def matches_elements(self, element):
        if isinstance(element, IsA):
            return Clause(
                [
                    Word("lo"),
                    self.translate(element.entity),
                    self.translate(element.category),
                ]
            )

        return None


lexicon.add_definition(Id, XianPronoun(Person.First, Number.Sing))


class XianLexicon(Lexicon):
    def translate(self, element) -> Union[Clause, Word]:
        print(element)
        print(type(element))

        if isinstance(element, Entity):
            if element.relation is not None:
                if isinstance(element.relation, Son):
                    return Clause(
                        [
                            Word("ni’•yu"),
                            Word("e"),
                            self.translate(element.relation.parent),
                        ]
                    )
                else:
                    raise NotImplementedError(
                        "Unhandled relation %s" % (element.relation)
                    )
            elif "name" in element.attributes:
                return Word(element.attributes["name"])
            else:
                raise NotImplementedError("That Entity is not supported yet")
        elif isinstance(element, Id):
            return XianPronoun(Person.First, Number.Sing)
        elif isinstance(element, IsA):
            return Clause(
                [
                    Word("lo"),
                    self.translate(element.entity),
                    self.translate(element.category),
                ]
            )
        elif isinstance(element, Also):
            return Clause(
                [
                    Word("lo"),
                    Word(".u’uth"),
                    self.translate(element.entity),
                    self.translate(element.category),
                ]
            )
        elif isinstance(element, Equivalent):
            return Clause(
                [Word("tii"), self.translate(element.a), self.translate(element.b),]
            )
        elif isinstance(element, Need):
            return Clause(
                [
                    Word("sya"),
                    self.translate(element.actor),
                    Word("yo"),
                    self.translate(element.clause),
                ]
            )
        elif isinstance(element, MemberOfState):
            return Clause(
                [
                    Word("lo"),
                    self.translate(element.member),
                    Word("nya•sao"),
                    Word("se"),
                    self.translate(element.state),
                ]
            )
        elif isinstance(element, Diplomat):
            return Word("nya’•p.ū•h’ue•sao")
        elif isinstance(element, Student):
            return Word("nyayan")
        elif isinstance(element, UnitedEmpireOfEarth):
            return Word("Sao•Hyūm")
        elif isinstance(element, Travel):
            if element.destination is not None:
                return Clause(
                    [
                        Word("o"),
                        Word(".uai"),
                        Word("nui"),
                        Word(element.destination.orthography[LanguageCode.Xian]),
                    ]
                )
            else:
                return Clause([Word("o"), Word(".uai")])
        else:
            raise NotImplementedError("Unhandled element type %s" % (element))
