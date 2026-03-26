from .nintendo import NintendoStore


class StoreFactory:
    def get_store(self, url: str):
        if "nintendo.co.kr" in url:
            return NintendoStore()
        return None
