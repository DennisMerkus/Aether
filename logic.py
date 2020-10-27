from typing import List, Tuple, Type


class Predicate(object):
    def __init__(self, symbol: str, terms: List[Tuple[str, List[Type]]]):
        self.symbol = symbol
        self.terms = terms


class Fact(object):
    def __init__(self, symbol: str, terms: List[str]):
        self.symbol = symbol
        self.terms = terms


class Rule(object):
    def __init__(self, head: Predicate, body: Predicate):
        self.head = head
        self.body = body
