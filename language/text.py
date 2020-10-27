from typing import List


class WrittenText(object):
    @property
    def text(self) -> str:
        return ""

    @property
    def tokens(self) -> List[str]:
        return []
