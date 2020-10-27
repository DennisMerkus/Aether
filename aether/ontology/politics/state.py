from aether.ontology.base import AbstractCategory, Relation

from aether.ontology.person import Person


class PoliticalState(AbstractCategory):
    def __init__(self, name: str):
        name = name


class MemberOfState(Relation):
    def __init__(self, member: Person, state: PoliticalState):
        self.member = member
        self.state = state
