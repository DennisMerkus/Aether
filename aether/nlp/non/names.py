import random

from aether.ontology.gender import Gender


male_first_names = ["Bárðr", "Bjarni", "Herjólfr", "Ingólfr"]
female_first_names = ["Þorgerðr"]

all_first_names = male_first_names + female_first_names

last_names = ["Bárðarson", "Herjólfssonar"]


class NameGenerator(object):
    def first_name(self, gender: Gender) -> str:
        if gender is Gender.Male:
            return random.choice(male_first_names)
        elif gender is Gender.Female:
            return random.choice(female_first_names)
        else:
            return random.choice(all_first_names)

    def last_name(self) -> str:
        return random.choice(last_names)
