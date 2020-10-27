from enum import Enum, auto

from typing import Dict, List

from omnilingual import LanguageCode

from aether.nlp.uxy.lexicon import XianLexicon, Clause
from aether.nlp.lexicon import Lexicon, Word
from aether.thought import Image


class SpeechAct(Enum):
    Statement = auto()
    Question = auto()
    Exclamation = auto()
    Request = auto()
    Command = auto()
    Suggestion = auto()


class NaturalLanguageGenerator(object):
    def __init__(self):
        self.lexicon: Dict[LanguageCode, Lexicon] = {LanguageCode.Xian: XianLexicon()}

    def write(self, thought: Image, language: LanguageCode) -> List[str]:
        # For each element in the Thought, translate it (entities, relations)
        # Go through the tree and translate each element until everything is translated
        # or something cannot be translated
        if language not in self.lexicon:
            raise NotImplementedError(
                "Language %s is not supported for language generation." % (language)
            )

        clauses = [
            self.lexicon[language].translate(relation) for relation in thought.relations
        ]

        # Once translated, reconcile grammar and word order
        # Realize the sentence
        if len(clauses) == 0:
            return []
        elif len(clauses) == 1:
            return self.realize(clauses[0]) + ["."]
        else:
            raise NotImplementedError()

    def realize(self, element) -> List[str]:
        if isinstance(element, Word):
            return [element.word]
        elif isinstance(element, Clause):
            words: List[str] = []

            for word in element.words:
                words.extend(self.realize(word))

            return words
        else:
            raise NotImplementedError()
