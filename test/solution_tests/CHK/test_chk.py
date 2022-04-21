from solutions.CHK.checkout_solution import checkout


class TestSum():
    # def test_single_sku(self):
    #     assert checkout('A') == 50

    # def test_single_sku_offer(self):
    #     assert checkout('AAA') == 130

    # def test_multiple_sku(self):
    #     assert checkout('ABCD') == 115

    # def test_multiple_offer(self):
    #     assert checkout('AAABCD') == 195

    # def test_multiple_offer_bs(self):
    #     assert checkout('BB') == 45

    # def test_special_offer(self):
    #     assert checkout('EEB') == 80

    # def test_2As_2Es_3Bs(self):
    #     assert checkout('AAAEEB') == 210

    # def test_all_As(self):
    #     assert checkout('AAAAAAAA') == 330

    # def test_double_2E(self):
    #     assert checkout('EE') == 80

    # def test_4E_2B(self):
    #     assert checkout('EEEEBB') == 160

    # def test_As(self):
    #     assert checkout('AAAAAAAAAA') == 400

    # def test_3Fs(self):
    #     assert checkout('FFF') == 20

    # def test_6Fs(self):
    #     assert checkout('FFFFFF') == 40

    # def test_4Uss(self):
    #     assert checkout('UUUU') == 120

    
    def test_3Rs_1Q(self):
        assert checkout('RRRQ') == 150

    def test_4Rs_1Q(self):
        assert checkout('RRRRQ') == 200

    def test_6Rs_2Qs(self):
        assert checkout('RRRRRRQQ') == 300

    def test_3Ns_1M(self):
        assert checkout('NNNM') == 120

    def test_3Qs(self):
         assert checkout('QQQ') == 80