from __future__ import annotations

from typing import Any, Callable, Dict, List, Type, Union


class Word(object):
    def __init__(self, word: str):
        self._word: str = word

    @property
    def word(self) -> str:
        return self._word


class Clause(object):
    def __init__(self, words: List[Union[Clause, Word]]):
        self.words = words


class Subject(Clause):
    pass


class Verb(Clause):
    pass


class Predicate(object):
    pass


class Sentence(object):
    pass


class Lexicon(object):
    def __init__(self):
        self.definitions: Dict[Type, Union[Clause, Word]] = {}

    def add_definition(self, concept: Type, definition: Union[Clause, Word]) -> None:
        self.definitions[concept] = definition

    def add_equivalence(
        self,
        concept: Callable[[Any], Union[Clause, Word]],
        matcher: Callable[[Any], bool],
        utterance: Union[Clause, Word],
    ) -> None:
        raise NotImplementedError()

    def translate(self, element):
        raise NotImplementedError()


class GrammaticalPattern(object):
    def __init__(self, element, words):
        self.element = element
        self.words = words

    def __eq__(self, other):
        if not isinstance(other, GrammaticalPattern):
            return False

        return self.elements == other.elements and self.words == other.words

    def matches_elements(self, element) -> bool:
        return self.element == element

    def matches_phrase(self, phrase) -> bool:
        pass


class GrammarLexicon(object):
    # Responsible for linear time lookup of grammar rules

    def add(self, pattern):
        raise NotImplementedError()

    # Find the (sub)patterns that match and link with the text
    def match_patterns(self, phrase):
        raise NotImplementedError()

    # Find grammatical patterns that match with the partial tokens to create a sentence
    def realize(self, tokens):
        raise NotImplementedError()
