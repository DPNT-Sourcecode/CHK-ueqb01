from solutions.CHK.checkout_solution import checkout


class TestSum():
    def test_single_sku(self):
        assert checkout('A') == 50

    def test_single_sku_offer(self):
        assert checkout('AAA') == 130


