from aether.ontology.base import Entity, Category


class Also(object):
    def __init__(self, entity: Entity, category: Category):
        self.entity = entity
        self.category = category


class Equivalent(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
