from aether.ontology.base import Relation
from aether.ontology.person import Person


class Son(Relation):
    def __init__(self, parent: Person):
        self.parent = parent
