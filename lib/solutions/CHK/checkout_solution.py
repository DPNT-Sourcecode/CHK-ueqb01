# noinspection PyShadowingBuiltins,PyUnusedLocal
# skus = unicode string
def checkout(skus):
    from collections import Counter
    from enum import Enum
    from typing import List, Dict

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
        price_table = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15,
            'E': 40
        }

        offers = [
            Offer(sku='A', offer_type=OfferType.LOWER_PRICE_OFFER, trigger_quantity=3, offer_price=130, sku_applied_to='A'),
            Offer(sku='A', offer_type=OfferType.LOWER_PRICE_OFFER, trigger_quantity=5, offer_price=200, sku_applied_to='A'),
            Offer(sku='E', offer_type=OfferType.FREE_SKU_OFFER, trigger_quantity=2, offer_price=None, sku_applied_to='B'),
        ]


        def __init__(self, sku_counts = Dict[str, int]) -> None:
            self.sku_counts = sku_counts 


        def calculate_total_cost(self):
            total_cost = 0

            for sku in self.sku_counts:
                quantity_purchased = self.sku_counts[sku]

                # check if offer applies to this sku
                offers_being_applied = dict()

                for offer in self.offers:
                    offers_being_applied[offer.sku] = offer









            # for sku in sku_counts:
            #     if sku not in price_table:
            #         return -1

            # for sku in sku_counts:
            #     quantity_purchased = sku_counts[sku]
            #     total_cost += price_table[sku].calculate_total_cost(quantity_purchased)
        
            # return total_cost

    
    # Solution
    sku_counts = Counter(skus)

    price_table = PriceTable(skus)

    return price_table.calculate_total_cost()


# def calculate_total_cost(self, quantity_purchased: int):
        #     if not self.offer_quantity or quantity_purchased < self.offer_quantity:
        #         return quantity_purchased * self.price

        #     basic_quantity = quantity_purchased % self.offer_quantity
        #     return basic_quantity * self.price + ((quantity_purchased - basic_quantity) / self.offer_quantity) * self.offer_price
   

