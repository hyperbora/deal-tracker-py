import re
from .base import Store, StoreType


class NintendoStore(Store):
    def __init__(self):
        super().__init__(StoreType.NINTENDO)

    def extract_id(self, url: str) -> str:
        match = re.search(r"/(\d+)", url)
        return match.group(1) if match else ""
