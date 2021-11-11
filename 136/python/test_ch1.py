import pytest
from ch1 import power_of_two, determine_two_friendly


class TestPowerOfTwo:
    def test_type_validation(self):
        with pytest.raises(TypeError):
            power_of_two(0.01)
        with pytest.raises(TypeError):
            power_of_two("1")
        with pytest.raises(TypeError):
            power_of_two()
        with pytest.raises(ValueError):
            power_of_two(-1)

    def test_powers_of_two(self):
        with pytest.raises(ValueError):
            power_of_two(0)

        assert power_of_two(2) == 1
        assert power_of_two(4) == 2
        assert power_of_two(8) == 3
        assert power_of_two(16) == 4
        assert power_of_two(32) == 5
        assert power_of_two(8192) == 13
        assert power_of_two(32768) == 15
        assert power_of_two(1099511627776) == 40

    def test_non_powers_of_two(self):
        assert power_of_two(1) == 0
        assert power_of_two(3) == 0
        assert power_of_two(6) == 0
        assert power_of_two(18) == 0
        assert power_of_two(4095) == 0
        assert power_of_two(8190) == 0


class TestDetermineTwoFriendly:
    def test_type_validation(self):
        with pytest.raises(TypeError):
            determine_two_friendly(0.01)
        with pytest.raises(TypeError):
            determine_two_friendly("1")
        with pytest.raises(TypeError):
            determine_two_friendly()
