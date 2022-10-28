from typing import Dict

from entity.base_storage import BaseStorage
from exceptions import TooManyDifferentProductsError

class Shop(BaseStorage):

    def __init__(self, items: Dict[str, int], capacity: int, max_unique_items: int):
        self.max_unique_items = max_unique_items
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        if self.get_unique_items_count() >= 5:
            raise TooManyDifferentProductsError

        super().add(name, amount)
