# Author: Max Radke         Date: 3/11/21

import calculator


class TestCalculator:

    def test_add(self):
        assert 5 == calculator.add(1, 4)

    def test_subtract(self):
        assert 2 == calculator.sub(5, 3)

    def text_multiply(self):
        assert 12 == calculator.mult(3, 4)
