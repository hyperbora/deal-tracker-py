import re
import requests
from .base import Store, StoreType, Price


class AppleAppStore(Store):
    def __init__(self):
        super().__init__(StoreType.APPLE_APP)
        self.api_url = "https://itunes.apple.com/lookup?id={id}&country=kr"

    def extract_id(self, url: str) -> str:
        match = re.search(r"id(\d+)", url)
        return match.group(1) if match else ""

    def get_price(self, product_id: str) -> Price:
        """API를 호출하여 가격 정보를 반환합니다."""
        try:
            url = self.api_url.format(id=product_id)
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()

            if data.get("resultCount", 0) == 0:
                return None

            result = data["results"][0]

            current_price = int(result.get("price", 0))

            return Price(regular=current_price, current=current_price)

        except (requests.RequestException, ValueError, KeyError, IndexError):
            return None
