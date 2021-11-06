import pytest
from ch1 import int_sqrt


class TestIntegerSquareRoot:
    def test_negatives(self):
        with pytest.raises(ValueError):
            int_sqrt(-1)

    def test_zero_and_one(self):
        assert int_sqrt(0) == 0
        assert int_sqrt(1) == 1

    def test_examples(self):
        assert int_sqrt(10) == 3
        assert int_sqrt(27) == 5
        assert int_sqrt(85) == 9
        assert int_sqrt(101) == 10

    def test_my_examples(self):
        assert int_sqrt(100) == 10
        assert int_sqrt(7) == 2
        assert int_sqrt(2) == 1
        assert int_sqrt(0.04) == 0
        assert int_sqrt(127) == 11
        assert int_sqrt(3.14159265) == 1
        assert int_sqrt(1.41421356) == 1
