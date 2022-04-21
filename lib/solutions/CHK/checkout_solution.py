from collections import Counter

class PriceData:
    def __init__(self, letter: str, price: int, offer_quantity: int = None, offer_price: int = None) -> None:
        self.letter = letter
        self.price = price
        self.offer_quantity = offer_quantity
        self.offer_price = offer_price

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

# noinspection PyShadowingBuiltins,PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # sku_counts = Counter(skus)

    # total_cost = 0

    # for sku in sku_counts:
    #     if sku not in price_table:
    #         return -1


    # for sku in sku_counts:
    #     quantity_purchased = sku_counts[sku]
    #     total_cost += price_table[sku].calculate_total_cost(quantity_purchased)
        
    # return total_cost

    return -1





   
