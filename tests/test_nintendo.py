import pytest
from src.stores.nintendo import NintendoStore


def test_nintendo_get_price_success(mocker):
    mock_response = {
        "country": "KR",
        "personalized": False,
        "prices": [
            {
                "gold_point": {
                    "basic_gift_gp": "0",
                    "basic_gift_rate": "0",
                    "consume_gp": "0",
                    "extra_gold_points": [],
                    "gift_gp": "0",
                    "gift_rate": "0",
                },
                "regular_price": {
                    "amount": "84,800원",
                    "currency": "KRW",
                    "raw_value": "84800",
                },
                "sales_status": "onsale",
                "title_id": 70010000096823,
            }
        ],
    }

    mock_get = mocker.patch("requests.get")

    mock_response_obj = mock_get.return_value
    mock_response_obj.status_code = 200
    mock_response_obj.json.return_value = mock_response  # json() 실행 시 데이터 반환

    store = NintendoStore()
    price_info = store.get_price("70010000096823")

    assert price_info is not None
    assert price_info.regular == 84800
    assert price_info.current == 84800
