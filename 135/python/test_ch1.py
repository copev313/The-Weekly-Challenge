import pytest
from ch1 import middle_three_digits


class TestMiddleThreeDigits:
    def test_type_validation(self):
        with pytest.raises(TypeError):
            middle_three_digits(0.01)
        with pytest.raises(TypeError):
            middle_three_digits("1")
        with pytest.raises(TypeError):
            middle_three_digits()

    def test_too_small_case(self):
        expected = "Number is too short."
        assert middle_three_digits(0) == expected
        assert middle_three_digits(-10) == expected
        assert middle_three_digits(-8) == expected
        assert middle_three_digits(7) == expected

    def test_even_digits_case(self):
        expected = "Number is even."
        assert middle_three_digits(1111) == expected
        assert middle_three_digits(1000000000) == expected
        assert middle_three_digits(-12233556) == expected

    def test_negative_numbers(self):
        assert middle_three_digits(-9876543210) == "Number is even."
        assert middle_three_digits(-90) == "Number is too short."
        assert middle_three_digits(-123) == '123'
        assert middle_three_digits(-9988877) == '888'
        assert middle_three_digits(100000000) == '000'

    def test_three_digit_nums(self):
        assert middle_three_digits(100) == '100'
        assert middle_three_digits(-100) == '100'
        assert middle_three_digits(987) == '987'
        assert middle_three_digits(314) == '314'

    def test_substring_logic(self):
        assert middle_three_digits(876543210) == '543'
        assert middle_three_digits(9765432109876543210) == '098'
        assert middle_three_digits(123456789) == '456'
        assert middle_three_digits(9876434614946550155461456) == '465'
