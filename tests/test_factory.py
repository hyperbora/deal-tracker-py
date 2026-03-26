import pytest
from src.stores.factory import StoreFactory
from src.stores.base import StoreType


def test_should_identify_nintendo_store():
    """닌텐도 스토어 URL을 넣었을 때 Nintendo 전용 객체를 반환하는지 확인"""
    factory = StoreFactory()
    url = "https://store.nintendo.co.kr/70010000096823"

    store = factory.get_store(url)

    assert store is not None
    assert store.store_type == StoreType.NINTENDO


def test_should_return_none_for_unknown_url():
    """지원하지 않는 URL을 넣었을 때 None을 반환하는지 확인"""
    factory = StoreFactory()
    url = "https://unknown-store.com/item/123"

    store = factory.get_store(url)

    assert store is None
