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
    letter_counts = Counter(skus)
    for letter in letter_counts:
        purchased_quantity = letter_counts[letter]




   


