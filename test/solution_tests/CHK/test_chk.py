from solutions.CHK.checkout_solution import checkout


class TestSum():
    def test_single_sku(self):
        assert checkout('A') == 50

    def test_single_sku_offer(self):
        assert checkout('AAA') == 130

    # def test_multiple_sku(self):
    #     assert checkout('ABCD') == 115

    # def test_multiple_offer(self):
    #     assert checkout('AAABCD') == 195

    # def test_multiple_offer_bs(self):
    #     assert checkout('BB') == 45

    # def test_special_offer(self):
    #     assert checkout('EEB') == 80

    # def test_special_offer(self):
    #     assert checkout('AAAEEB') == 210

    # def test_As(self):
    #     assert checkout('AAAAAAAA') == 330

    # def test_special_offer(self):
    #     assert checkout('AAAAAAAA') == 210

    
    
