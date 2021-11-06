import pytest
from ch1 import is_pandigital, pandigital_nums


class TestIsPandigital:
    def test_type_validation(self):
        with pytest.raises(TypeError):
            is_pandigital(0.01)
        with pytest.raises(TypeError):
            is_pandigital("1")
        with pytest.raises(TypeError):
            is_pandigital()

    def test_small_pandigital(self):
        assert is_pandigital(123) is False
        assert is_pandigital(12345678) is False
        assert is_pandigital(0) is False
        assert is_pandigital(1023456789) is True

    def test_large_pandigital(self):
        assert is_pandigital(9876543210) is True
        assert is_pandigital(98765432109876543210) is True


class TestPandigitalNums:
    def test_input_validation(self):
        assert pandigital_nums(0) == []
        with pytest.raises(ValueError):
            pandigital_nums(-1)

    def test_first_5_numbers(self):
        pand_numbers = [1023456789,
                        1023456798,
                        1023456879,
                        1023456897,
                        1023456978,
                        1023456987,
                        1023457689]
        assert pandigital_nums(2) == pand_numbers[0:2]
        assert pandigital_nums(3) == pand_numbers[0:3]
        assert pandigital_nums(5) == pand_numbers[0:5]
        assert pandigital_nums(7) == pand_numbers[0:7]
