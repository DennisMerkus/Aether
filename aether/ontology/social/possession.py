from aether.ontology.base import Relation
from aether.ontology.person import Person


class OwnedBy(Relation):
    def __init__(self, owner: Person):
        self.owner = owner
