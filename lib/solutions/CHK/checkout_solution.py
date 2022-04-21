from collections import Counter


class PriceData:
    def __init__(self, letter: str, price: int, offer_quantity: int = None, offer_price: int = None) -> None:
        self.letter = letter
        self.price = price
        self.offer_quantity = offer_quantity
        self.offer_price = offer_price


price_table = {
    'A': PriceData('A', 50, 3, 130),
    'B': PriceData('B', 30, 2, 45),
    'C': PriceData('C', 20),
    'D': PriceData('D', 15),
}

# noinspection PyShadowingBuiltins,PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_counts = Counter(skus)

    total_price = 0

    for sku in sku_counts:
        purchased_quantity = sku_counts[sku]
        offer_quantity = price_table[sku].offer_quantity
        offer_price = price_table[sku].offer_price
        basic_price = price_table[sku].price
        basic_quantity = purchased_quantity % offer_quantity

        sku_cost =  basic_quantity * basic_price + ((purchased_quantity - basic_quantity) / offer_quantity) * offer_price

        total_price += sku_cost

    return total_price





   




