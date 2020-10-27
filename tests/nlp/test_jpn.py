import unittest

from typing import List

from aether.thought import Image
from aether.nlp.nlg import NaturalLanguageGenerator

from aether.ontology.base import AtLocation
from aether.ontology.special import Id

from aether.ontology.occupation.education import School, Study

from aether.ontology.worlds.earth.language import JapaneseLanguage

from omnilingual import LanguageCode


class TestJapaneseJlptN5(unittest.TestCase):
    # https://jlptsensei.com/jlpt-n5-grammar-list/

    def test_de_place_of_action(self):
        # https://jlptsensei.com/learn-japanese-grammar/%e3%81%a7-de-particle-meaning/
        # 学校で日本語を勉強する。
        thought = Image(AtLocation(School(), Study(Id(), JapaneseLanguage())))

        # Option: Omit subject
        # Option: Location first
        # Option: Casual register

        nlg = NaturalLanguageGenerator()

        words: List[str] = nlg.write(thought, LanguageCode.Japanese)

        self.assertEqual(words, ["学校", "で", "日本語", "を", "勉強", "している", "。"])
