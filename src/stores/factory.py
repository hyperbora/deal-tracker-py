from .nintendo import NintendoStore
from .apple import AppleAppStore


class StoreFactory:
    def get_store(self, url: str):
        if "nintendo.co.kr" in url:
            return NintendoStore()
        if "apps.apple.com" in url:
            return AppleAppStore()
        return None
