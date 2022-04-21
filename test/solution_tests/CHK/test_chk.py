from solutions.CHK.checkout_solution import checkout


class TestSum():
    def test_A(self):
        assert checkout('A') == 50

    def test_AAA(self):
        assert checkout('AAA') == 130

    def test_ABCD(self):
        assert checkout('ABCD') == 115

    def test_AAABCD(self):
        assert checkout('AAABCD') == 195

    def test_BB(self):
        assert checkout('BB') == 45

    def test_EEB(self):
        assert checkout('EEB') == 80

    def test_AAAEEB(self):
        assert checkout('AAAEEB') == 210

    def test_AAAAAAAA(self):
        assert checkout('AAAAAAAA') == 330

    def test_EE(self):
        assert checkout('EE') == 80

    def test_EEEEBB(self):
        assert checkout('EEEEBB') == 160

    def test_AAAAAAAAAA(self):
        assert checkout('AAAAAAAAAA') == 400

    def test_FFF(self):
        assert checkout('FFF') == 20

    def test_FFFFFF(self):
        assert checkout('FFFFFF') == 40

    def test_UUUU(self):
        assert checkout('UUUU') == 120

    def test_RRRQ(self):
        assert checkout('RRRQ') == 150

    def test_RRRRQ(self):
        assert checkout('RRRRQ') == 200

    def test_RRRRRRQQ(self):
        assert checkout('RRRRRRQQ') == 300

    def test_NNNM(self):
        assert checkout('NNNM') == 120

    def test_QQQ(self):
         assert checkout('QQQ') == 80

    def test_STXYZ(self):
         assert checkout('STXYZ') == 82

    def test_SSS(self):
         assert checkout('SSS') == 45