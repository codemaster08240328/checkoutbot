from typing import Callable, List
from entities import Checkout

class Checkouts:
    items: List[Checkout]

    def __init__(self):
        self.items = []

    def add(self, cust_id: str, item_id: str):
        self.items.append(Checkout(cust_id, item_id))
      
    def remove(self, cust_id: str):
        func: Callable[[Checkout], bool] = lambda checkout: checkout.customer_id != cust_id
        self.items = list(filter(func, self.items))  
        pass

    def clear(self):
        self.items = []
