from typing import Dict

from omnilingual import LanguageCode

from aether.ontology.base import Category


class Location(object):
    orthography: Dict[LanguageCode, str]

    def __init__(self):
        self.orthography = {}


class Headland(Category):
    pass


class Land(Category):
    pass

