from typing import Optional

from aether.ontology.geography import Location


class Travel(object):
    def __init__(self, destination: Optional[Location] = None):
        self.destination = destination
