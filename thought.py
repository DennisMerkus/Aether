from typing import Optional

from aether.ontology.base import Relation


class Time(object):
    pass


class AmbiguousTime(Time):
    pass


class Now(Time):
    pass


class Future(Time):
    pass


class Image(object):
    def __init__(self, time: Time, relation: Optional[Relation] = None):
        self.time: Time = time
        self.relations = []

        if relation is not None:
            self.relations.append(relation)


class Event(object):
    pass


class Sequence(object):
    # Sequence of events
    pass
