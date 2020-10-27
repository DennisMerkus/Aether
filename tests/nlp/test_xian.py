import unittest
from typing import List

from omnilingual import LanguageCode

from aether.nlp.nlg import NaturalLanguageGenerator
from aether.nlp.nli import NaturalLanguageInterpreter
from aether.ontology.base import Entity, IsA, QueryProperty
from aether.ontology.bdi import Need
from aether.ontology.family import Son
from aether.ontology.life.house import House
from aether.ontology.misc import Also, Equivalent
from aether.ontology.movement.general import Travel
from aether.ontology.occupation.education import Student
from aether.ontology.occupation.politics import Diplomat
from aether.ontology.politics.state import MemberOfState
from aether.ontology.sense.vision.color import Color
from aether.ontology.social.possession import OwnedBy
from aether.ontology.special import Id, Listener
from aether.ontology.worlds.starcitizen.empires import UnitedEmpireOfEarth
from aether.ontology.worlds.starcitizen.geography import Cawa
from aether.thought import Image


class TestXianBasicSentences(unittest.TestCase):
    def test_generates_citizen_of_UEE(self):
        # I am a citizen of the UEE.
        thought = Image(MemberOfState(Id(), UnitedEmpireOfEarth()))

        nlg = NaturalLanguageGenerator()

        words: List[str] = nlg.write(thought, LanguageCode.Xian)

        self.assertEqual(words, ["lo", "no’a", "nya•sao", "se", "Sao•Hyūm", "."])

    def test_interprets_citizen_of_UEE(self):
        words = ["lo", "no’a", "nya•sao", "se", "Sao•Hyūm", "."]

        nli = NaturalLanguageInterpreter()

        thought = nli.interpret(words)

        self.assertEqual(thought, Image(MemberOfState(Id(), UnitedEmpireOfEarth())))

    def test_son_is_also_diplomat(self):
        # My son is also a diplomat.
        nlg = NaturalLanguageGenerator()
        words: List[str] = nlg.write(
            Image(Also(Entity(Son(Id())), Diplomat())), LanguageCode.Xian
        )

        self.assertEqual(
            words, ["lo", ".u’uth", "ni’•yu", "e", "no’a", "nya’•p.ū•h’ue•sao", "."],
        )

    def test_Mylo_is_my_son(self):
        # Mylo is my son.
        nlg = NaturalLanguageGenerator()
        words: List[str] = nlg.write(
            Image(Equivalent(Entity(attributes={"name": "Mai•lo"}), Entity(Son(Id())))),
            LanguageCode.Xian,
        )

        self.assertListEqual(
            words, ["tii", "Mai•lo", "ni’•yu", "e", "no’a", "."],
        )

    def test_I_need_to_go_to_Cawa(self):
        # I need to go to Cáwa.
        nlg = NaturalLanguageGenerator()
        words: List[str] = nlg.write(
            Image(Need(Id(), Travel(Cawa()))), LanguageCode.Xian
        )

        self.assertListEqual(
            words, ["sya", "no’a", "yo", "o", ".uai", "nui", "Ka’•ua", "."],
        )


class TestXianVerbs(unittest.TestCase):
    def test_lo_student(self):
        # I am a student.
        nlg = NaturalLanguageGenerator()

        words: List[str] = nlg.write(Image(IsA(Id(), Student())), LanguageCode.Xian)

        self.assertListEqual(words, ["lo", "no’a", "nyayan", "."])

    def test_lo_Xian(self):
        # I am a student.
        nlg = NaturalLanguageGenerator()

        words: List[str] = nlg.write(Image(), LanguageCode.Xian)

        self.assertListEqual(words, ["lo", "no’a", "nya", "se", "Xi’an" "."])

    def test_lo_Xyan(self):
        # I am a student.
        nlg = NaturalLanguageGenerator()

        words: List[str] = nlg.write(Image(), LanguageCode.Xian)

        self.assertListEqual(words, ["lo", "no’a", "Xy’an" "."])

    def test_tii_1_plus_2_is_3(self):
        # 1 plus 2 is 3.
        nlg = NaturalLanguageGenerator()

        words: List[str] = nlg.write(Image(), LanguageCode.Xian)

        self.assertListEqual(words, ["tii", "yath", "u", "syen", "p.uai", "."])

    def test_tii_your_mother(self):
        # She's Sunáth. ("The one who is Sunáth is my mother.")
        nlg = NaturalLanguageGenerator()

        words: List[str] = nlg.write(Image(), LanguageCode.Xian)

        self.assertListEqual(words, ["tii", "Su.n’ath", "."])

    def test_tii_head_of_department(self):
        # Who is the head of the department?
        # Theso and Tilá are co-chairs of the department.
        nlg = NaturalLanguageGenerator()

        words: List[str] = nlg.write(Image(), LanguageCode.Xian)

        self.assertListEqual(words, ["tii", "Su.n’ath", "uth", "Ti.l’a", "."])

    def test_tii_teachers(self):
        # Who here are teachers (asked with tii)?
        # (Theso and Tilá are teachers..., but I’m not sure about the rest.)
        nlg = NaturalLanguageGenerator()

        words: List[str] = nlg.write(Image(), LanguageCode.Xian)

        self.assertListEqual(
            words, ["lo", "The’so", "uth", "Ti.l’a", "nya’to.y’an", "."]
        )

    def test_e_what_color_house(self):
        # What color is your house?
        nlg = NaturalLanguageGenerator()

        words: List[str] = nlg.write(
            Image(QueryProperty(House(OwnedBy(Listener())), Color)), LanguageCode.Xian,
        )

        self.assertListEqual(words, ["e", "n.aoxy.oa", "tā", "e", "lē", "?"])
