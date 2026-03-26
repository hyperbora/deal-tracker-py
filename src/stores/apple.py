import re
from .base import Store, StoreType


class AppleAppStore(Store):
    def __init__(self):
        super().__init__(StoreType.APPLE_APP)

    def extract_id(self, url: str) -> str:
        match = re.search(r"id(\d+)", url)
        return match.group(1) if match else ""
