def checkout(skus):
    from collections import Counter
    from enum import Enum
    import itertools

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

    price_table = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40
    }

    offers = {
        'A': [
            Offer(sku='A', offer_type=OfferType.LOWER_PRICE_OFFER, trigger_quantity=3, offer_price=130, sku_applied_to='A'),
            Offer(sku='A', offer_type=OfferType.LOWER_PRICE_OFFER, trigger_quantity=5, offer_price=200, sku_applied_to='A'),
        ],

        'B': [
            Offer(sku='B', offer_type=OfferType.LOWER_PRICE_OFFER, trigger_quantity=2, offer_price=45, sku_applied_to='B'),
        ],

        'E': [
            Offer(sku='E', offer_type=OfferType.FREE_SKU_OFFER, trigger_quantity=2, offer_price=None, sku_applied_to='B')
        ]
    }
    
    def calculate_total_cost(sku_counts):
        total_cost = float('inf')

        offer_combinations = list(itertools.product(*offers.values()))

        for combo in offer_combinations:
            total_cost_for_combo = 0

            sku_to_offer_map = dict()
            
            for offer in combo:
                sku_to_offer_map[offer.sku] = offer

            total_costs_per_sku = {
                'A': 0,
                'B': 0,
                'C': 0,
                'D': 0,
                'E': 0
            }

            # calculate total cost for each sku
            for sku in sku_counts:
                quantity_purchased = sku_counts[sku]

                # check if offer applies to the sku
                if sku in sku_to_offer_map:
                    if sku_counts[sku] == 0:
                        continue

                    sku_offer = sku_to_offer_map[sku]
                    
                    if sku_offer.offer_type == OfferType.LOWER_PRICE_OFFER:
                        basic_quantity = quantity_purchased % sku_offer.trigger_quantity
                        total_costs_per_sku[sku] += basic_quantity * price_table[sku] + ((quantity_purchased - basic_quantity) / sku_offer.trigger_quantity) * sku_offer.offer_price
                    
                    elif sku_offer.offer_type == OfferType.FREE_SKU_OFFER:
                        basic_quantity = quantity_purchased % sku_offer.trigger_quantity
                        total_costs_per_sku[sku_offer.sku_applied_to] -= ((quantity_purchased - basic_quantity) / sku_offer.trigger_quantity) * price_table[sku_offer.sku_applied_to]
                        total_costs_per_sku[sku] += quantity_purchased * price_table[sku]      
                else:
                    total_costs_per_sku[sku] += quantity_purchased * price_table[sku]

            total_cost_for_combo = sum(x if x >= 0 else 0 for x in total_costs_per_sku.values())

            total_cost = min(total_cost_for_combo, total_cost)

        return total_cost
    
    # Solution
    return calculate_total_cost(Counter(skus))
   

