from typing import Dict, Optional, Type


class Category(object):
    pass


class AbstractCategory(object):
    pass


class Relation(object):
    pass


class Property(object):
    pass


class Entity(object):
    def __init__(
        self,
        relation: Optional[Relation] = None,
        attributes: Dict[str, str] = {},
    ):
        self.relation: Optional[Relation] = relation

        self.attributes: Dict[str, str] = attributes


class IsA(object):
    def __init__(self, entity: Entity, category: Category):
        self.entity = entity
        self.category = category


class HasProperty(object):
    def __init__(self, entity: Entity, prop: Property):
        self.entity = entity
        self.property = prop


class Variable(object):
    def __init__(self, symbol: str):
        self.symbol = symbol

    def __eq__(self, other):
        if not isinstance(other, Variable):
            return False

        return self.symbol == other.symbol


class Query(object):
    def __init__(self, variable: Variable, clause):
        self.variable = variable
        self.clause = clause


class QueryProperty(object):
    def __init__(self, entity: Entity, prop: Type[Property]):
        self.entity = entity
        self.property = prop


class Reference(object):
    def __init__(self, ambiguous: bool = False):
        self.ambiguous = ambiguous


class AtLocation(object):
    def __init__(self, location, clause):
        self.clause = clause
        self.location = location
