# noinspection PyShadowingBuiltins,PyUnusedLocal
# skus = unicode string
def checkout(skus):
    from collections import Counter
    from enum import Enum
    from typing import List

    class OfferType(Enum):
        LOWER_PRICE_OFFER = 1
        FREE_SKU_OFFER = 2

    class Offer:
        def __init__(self, sku: str, offer_type: 'OfferType', trigger_quantity: int, offer_price: int, sku_applied_to: str = None) -> None:
            self.sku = sku
            self.offer_type = offer_type
            self.trigger_quantity = trigger_quantity
            self.offer_price = offer_price
            self.sku_applied_to = sku_applied_to

    class PriceTable:
        def __init__(self, letter: str, price: int, offer_quantity: int = None, offer_price: int = None) -> None:
            self.price_table = {
                'A': 50,
                'B': 30,
                'C': 20,
                'D': 15
            }





        def calculate_total_cost(self, quantity_purchased: int):
            if not self.offer_quantity or quantity_purchased < self.offer_quantity:
                return quantity_purchased * self.price

            basic_quantity = quantity_purchased % self.offer_quantity
            return basic_quantity * self.price + ((quantity_purchased - basic_quantity) / self.offer_quantity) * self.offer_price


    price_table = {
        'A': PriceData('A', 50, 3, 130),
        'B': PriceData('B', 30, 2, 45),
        'C': PriceData('C', 20),
        'D': PriceData('D', 15),
    }

    sku_counts = Counter(skus)

    total_cost = 0

    for sku in sku_counts:
        if sku not in price_table:
            return -1


    for sku in sku_counts:
        quantity_purchased = sku_counts[sku]
        total_cost += price_table[sku].calculate_total_cost(quantity_purchased)
        
    return total_cost




   




