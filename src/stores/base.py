from enum import Enum
from abc import ABC, abstractmethod


class StoreType(Enum):
    NINTENDO = "NINTENDO"
    APPLE_APP = "APPLE_APP"
    UNKNOWN = "UNKNOWN"


class Store(ABC):
    def __init__(self, store_type: StoreType):
        self.store_type = store_type

    @property
    def name(self):
        return self.store_type.value

    @abstractmethod
    def extract_id(self, url: str) -> str:
        pass
