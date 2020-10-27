from typing import Any, Optional

from aether.ontology.base import Category, Relation

from aether.ontology.person import Person


class Student(Category):
    pass


class School(Category):
    pass


class Study(Relation):
    def __init__(self, person: Person, subject: Optional[Any] = None):
        self.person = person
        self.subject = subject
