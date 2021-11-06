import pytest
from ch2 import generate_smith_numbers, prime_factors, smith_number


class TestPrimeFactorization:
    def test_prime_examples(self):
        assert prime_factors(1) == []
        assert prime_factors(2) == [2]
        assert prime_factors(3) == [3]
        assert prime_factors(7) == [7]
        assert prime_factors(199) == [199]

    def test_input_validation(self):
        with pytest.raises(ValueError):
            prime_factors(-1)
        with pytest.raises(ValueError):
            prime_factors(0)

    def test_prime_factors(self):
        assert prime_factors(4) == [2, 2]
        assert prime_factors(13) == [13]
        assert prime_factors(165113) == [13, 13, 977]
        assert prime_factors(13581965) == [5, 2716393]
        assert prime_factors(123456) == [2, 2, 2, 2, 2, 2, 3, 643]


class TestSmithNumber:
    def test_all_trues(self):
        assert smith_number(4) is True
        assert smith_number(22) is True
        assert smith_number(121) is True
        assert smith_number(346) is True
        assert smith_number(1086) is True

    def test_all_falses(self):
        assert smith_number(5) is False
        assert smith_number(23) is False
        assert smith_number(122) is False
        assert smith_number(347) is False
        assert smith_number(1087) is False

    def test_mixed_results(self):
        assert smith_number(3) is False
        assert smith_number(94) is True
        assert smith_number(200) is False
        assert smith_number(517) is True
        assert smith_number(895) is True

    def test_input_validation(self):
        with pytest.raises(ValueError):
            smith_number(-1)
        with pytest.raises(ValueError):
            smith_number(0)


class TestGenerateSmithNumbers:
    def test_zero(self):
        assert generate_smith_numbers(0) == []

    def test_input_validation(self):
        with pytest.raises(ValueError):
            generate_smith_numbers(-1)

    def test_generate_smith_numbers(self):
        assert generate_smith_numbers(1) == [4]
        assert generate_smith_numbers(5) == [4, 22, 27, 58, 85]
        assert generate_smith_numbers(10) == [4, 22, 27, 58, 85, 94, 121,
                                              166, 202, 265]
        assert generate_smith_numbers(20) == [4, 22, 27, 58, 85, 94, 121,
                                              166, 202, 265, 274, 319, 346,
                                              355, 378, 382, 391, 438, 454,
                                              483]
