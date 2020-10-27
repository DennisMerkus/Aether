from omnilingual import LanguageCode

from aether.ontology.geography import Location


class Cawa(Location):
    def __init__(self):
        super().__init__()

        self.orthography.update(
            {LanguageCode.Xian: "Ka’•ua", LanguageCode.English: "Cáwa"}
        )
