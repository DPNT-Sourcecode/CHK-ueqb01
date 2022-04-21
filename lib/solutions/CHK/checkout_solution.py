def checkout(skus):
    from collections import Counter
    from enum import Enum

    class OfferType(Enum):
        LOWER_PRICE_OFFER = 1
        FREE_SKU_OFFER = 2
        BUY_X_GET_1_FREE = 3
        GROUP_OFFER = 4

    class Offer:
        def __init__(self, sku: str, offer_type: 'OfferType', trigger_quantity: int, offer_price: 
                            int, sku_applied_to: str = None, x: int = None, group = ['S', 'T', 'X', 'Y', 'Z']) -> None:
            self.sku = sku
            self.offer_type = offer_type
            self.trigger_quantity = trigger_quantity
            self.offer_price = offer_price
            self.sku_applied_to = sku_applied_to
            self.x = x
            self.group = group

        def __str__(self) -> str:
            return f'{self.sku}-{self.offer_price}-{self.trigger_quantity}'

        def __repr__(self) -> str:
            return self.__str__()

    price_table = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 80,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50
    }

    offers = {
        'A': [
            Offer(sku='A', offer_type=OfferType.LOWER_PRICE_OFFER,
                  trigger_quantity=3, offer_price=130, sku_applied_to='A'),
            Offer(sku='A', offer_type=OfferType.LOWER_PRICE_OFFER,
                  trigger_quantity=5, offer_price=200, sku_applied_to='A'),
        ],

        'B': [
            Offer(sku='B', offer_type=OfferType.LOWER_PRICE_OFFER,
                  trigger_quantity=2, offer_price=45, sku_applied_to='B'),
            # 2E get one B free
            Offer(sku='B', offer_type=OfferType.FREE_SKU_OFFER,
                  trigger_quantity=2, offer_price=0, sku_applied_to='E')
        ],

        'F': [
            # 2F get one F free
            Offer(sku='F', offer_type=OfferType.BUY_X_GET_1_FREE,
                  trigger_quantity=3, offer_price=0, sku_applied_to='F', x=2)
        ],
        'H': [
            Offer(sku='H', offer_type=OfferType.LOWER_PRICE_OFFER,
                  trigger_quantity=5, offer_price=45, sku_applied_to='H'),
            Offer(sku='H', offer_type=OfferType.LOWER_PRICE_OFFER,
                  trigger_quantity=10, offer_price=80, sku_applied_to='H'),
        ],
        'K': [
            Offer(sku='K', offer_type=OfferType.LOWER_PRICE_OFFER,
                  trigger_quantity=2, offer_price=150, sku_applied_to='K'),
        ],

        'M': [
            # 3N get one M free
            Offer(sku='M', offer_type=OfferType.FREE_SKU_OFFER,
                  trigger_quantity=3, offer_price=0, sku_applied_to='N')
        ],

        'P': [
            Offer(sku='P', offer_type=OfferType.LOWER_PRICE_OFFER,
                  trigger_quantity=5, offer_price=200, sku_applied_to='P'),
        ],

        'Q': [
            # 3R get one Q free
            Offer(sku='Q', offer_type=OfferType.FREE_SKU_OFFER,
                  trigger_quantity=3, offer_price=0, sku_applied_to='R'),
            Offer(sku='Q', offer_type=OfferType.LOWER_PRICE_OFFER,
                  trigger_quantity=3, offer_price=80, sku_applied_to='Q'),
        ],

        'U': [
            # 2F get one F free
            Offer(sku='U', offer_type=OfferType.BUY_X_GET_1_FREE,
                  trigger_quantity=4, offer_price=0, sku_applied_to='U', x=3)
        ],

        'V': [
            Offer(sku='V', offer_type=OfferType.LOWER_PRICE_OFFER,
                  trigger_quantity=2, offer_price=90, sku_applied_to='V'),
            Offer(sku='V', offer_type=OfferType.LOWER_PRICE_OFFER,
                  trigger_quantity=3, offer_price=130, sku_applied_to='V'),
        ],

        # Group Offers
        'S': [Offer(sku='S', offer_type=OfferType.GROUP_OFFER,
                  trigger_quantity=3, offer_price=45, sku_applied_to='S')],
        
        'T': [Offer(sku='T', offer_type=OfferType.GROUP_OFFER,
                  trigger_quantity=3, offer_price=45, sku_applied_to='T')],

         'X': [Offer(sku='X', offer_type=OfferType.GROUP_OFFER,
                  trigger_quantity=3, offer_price=45, sku_applied_to='X')],

        'Y': [Offer(sku='Y', offer_type=OfferType.GROUP_OFFER,
                  trigger_quantity=3, offer_price=45, sku_applied_to='Y')],

        'Z': [Offer(sku='Z', offer_type=OfferType.GROUP_OFFER,
                  trigger_quantity=3, offer_price=45, sku_applied_to='Z')],


    }

    def calculate_total_cost(sku_counts):
        for sku in sku_counts:
            if sku not in price_table:
                return -1

        total_cost = 0

        for sku in sku_counts:
            quantity_purchased = sku_counts[sku]
            total_cost += quantity_purchased * price_table[sku]

        # calculate reduction in cost
        for sku in sku_counts:
            if sku not in offers:
                continue

            sku_offers = offers[sku]

            # order offers by price per unit
            sku_offers.sort(key=lambda x: x.offer_price/x.trigger_quantity)

            for _, offer in enumerate(sku_offers):
                while sku_counts[sku] > 0:
                    if offer.offer_type == OfferType.LOWER_PRICE_OFFER and sku_counts[sku] >= offer.trigger_quantity:
                        total_cost = total_cost - \
                            (price_table[sku] *
                             offer.trigger_quantity) + offer.offer_price
                        sku_counts[sku] -= offer.trigger_quantity

                    elif offer.offer_type == OfferType.FREE_SKU_OFFER and sku_counts[offer.sku_applied_to] >= offer.trigger_quantity:
                        total_cost = total_cost - price_table[sku]
                        sku_counts[offer.sku_applied_to] -= offer.trigger_quantity
                        sku_counts[sku] -= 1

                    elif offer.offer_type == OfferType.BUY_X_GET_1_FREE and sku_counts[offer.sku_applied_to] >= offer.trigger_quantity:
                        total_cost = total_cost - price_table[sku]
                        sku_counts[offer.sku_applied_to] -= offer.x
                        sku_counts[sku] -= 1

                    elif offer.offer_type == OfferType.GROUP_OFFER:
                        bundle = []
                        for c in offer.group:
                            if c in sku_counts and sku_counts[c] > 0:
                                bundle.append({c: price_table[c]})
                        
                                # bundle.sort(key=lambda k, v: v) 

                                print(bundle, price_table)

                        break

                    else:
                        break

        return total_cost

    # Solution
    return calculate_total_cost(Counter(skus))

