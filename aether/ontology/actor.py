# lo no’a nyasao se SaoHyūm.
# I am a citizen of the UEE

from aether.logic import Fact, Predicate, Rule
from .person import Person
from .state import State


class Beliefs(object):
    def are_consistent_with(self, statement) -> bool:
        raise NotImplementedError()


class Drives(object):
    def instill(self, drive) -> None:
        raise NotImplementedError()


class Actor(object):
    beliefs = Beliefs()
    drives = Drives()


class Habitat(object):
    pass


class City(Habitat):
    pass


class Town(Habitat):
    pass


class Residence(object):
    pass


class Building(object):
    pass


class House(Building, Residence):
    pass


member = Predicate("MemberOfState", [("x", [Person]), ("y", [State])])
inhabits = Predicate("Inhabits", [("x", [Person]), ("y", [Habitat, Residence])])
citizen = Predicate("Citizen", [("x", [Person]), ("y", [State])])

# member_of_state(x: Person, y: State) -> citizen(x: Person, y: State)
Rule(citizen, member)

Fact("MemberOfState", ["id", "UEE"])

# Xian:
# citizen(X, Y) -> [nya•sao, se, $Y]
