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
