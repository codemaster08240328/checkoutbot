from typing import List, Callable
from entities import RegisterType, Checkout

class Registers:
    registers: RegisterType = {}

    def __init__(self) -> None:
        for index in range(25):
            self.registers[index] = []

    def assign(self, cust_id) -> None:
        for values in self.registers.values():
            if cust_id in values:
                return

        min_len = 0
        index = 0
        while min_len < len(self.registers[index]):
            index += 1
            if index == 25:
                index = 0
                min_len += 1
        
        self.registers[index].append(cust_id)

    def remove(self, cust_id) -> None:
        for key in self.registers.keys():
            if cust_id in self.registers[key]:
                self.registers[key].remove(cust_id)
                return

    def display(self, checkouts: List[Checkout]) -> RegisterType:
        display_registers: RegisterType = {}
        for key in self.registers.keys():
            display_registers[key] = []
        
            for cust_id in self.registers[key]:
                func: Callable[[Checkout], bool] = lambda checkout: checkout.customer_id == cust_id
                filtered_item = [checkout.item_id for checkout in list(filter(func, checkouts))]
                display_registers[key] += filtered_item

        return display_registers

    def clear(self) -> None:
        for index in range(25):
            self.registers[index] = []
