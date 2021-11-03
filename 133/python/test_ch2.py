import pytest
from ch2 import prime_factors, smith_number, generate_smith_numbers


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
        assert smith_number(4) == True
        assert smith_number(22) == True
        assert smith_number(121) == True
        assert smith_number(346) == True
        assert smith_number(1086) == True

    def test_all_falses(self):
        assert smith_number(5) == False
        assert smith_number(23) == False
        assert smith_number(122) == False
        assert smith_number(347) == False
        assert smith_number(1087) == False

    def test_mixed_results(self):
        assert smith_number(3) == False
        assert smith_number(94) == True
        assert smith_number(200) == False
        assert smith_number(517) == True
        assert smith_number(895) == True

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

