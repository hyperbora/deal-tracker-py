import pytest
from src.stores.apple import AppleAppStore
from src.stores.base import Price


def test_apple_get_price_success(mocker):
    # 실제 응답과 동일한 구조의 Mock 데이터
    mock_response = {
        "resultCount": 1,
        "results": [{"trackId": 6502453075, "price": 9800.00, "currency": "KRW"}],
    }

    mock_get = mocker.patch("requests.get")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    store = AppleAppStore()
    price_info = store.get_price("6502453075")

    assert isinstance(price_info, Price)
    assert price_info.current == 9800
    assert price_info.regular == 9800
