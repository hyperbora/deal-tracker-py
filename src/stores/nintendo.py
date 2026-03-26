import re
import requests
from .base import Store, StoreType, Price


class NintendoStore(Store):
    def __init__(self):
        super().__init__(StoreType.NINTENDO)
        # 닌텐도 코리아 공식 API 엔드포인트 예시
        self.api_url = "https://api.ec.nintendo.com/v1/price?country=KR&lang=ko&ids="

    def extract_id(self, url: str) -> str:
        """URL에서 상품 고유 ID(숫자)를 추출합니다."""
        match = re.search(r"/(\d+)", url)
        return match.group(1) if match else ""

    def get_price(self, product_id: str) -> Price:
        """실제 API를 호출하여 정가와 현재가를 가져옵니다."""
        try:
            response = requests.get(f"{self.api_url}{product_id}", timeout=10)
            response.raise_for_status()  # 4xx, 5xx 에러 시 예외 발생

            data = response.json()

            # API 구조: data['prices'] 리스트의 첫 번째 항목 사용
            if not data.get("prices") or len(data["prices"]) == 0:
                return None

            price_info = data["prices"][0]

            # 정가(Regular Price) 추출
            reg_raw = price_info.get("regular_price", {}).get("raw_value", "0")

            # 현재가(Current Price) 추출
            # (만약 세일 중이라면 다른 키가 있을 수 있으나, 우선 기본 구조 기준)
            # 보통 세일 중이면 'discount_price' 같은 키가 추가되기도 함
            cur_raw = price_info.get("discount_price", {}).get("raw_value", reg_raw)

            return Price(regular=int(reg_raw), current=int(cur_raw))

        except (requests.RequestException, ValueError, KeyError, IndexError):
            # 네트워크 에러나 파싱 에러 발생 시 None 반환
            return None
