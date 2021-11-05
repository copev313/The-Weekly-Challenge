import pytest
from ch2 import gen_mult_matrix, print_results


class TestGenMultMatrix:
    def test_input_validation(self):
        with pytest.raises(ValueError):
            gen_mult_matrix(0, 0)
        with pytest.raises(TypeError):
            gen_mult_matrix()
        with pytest.raises(TypeError):
            gen_mult_matrix(0.1, 10)
        with pytest.raises(ValueError):
            gen_mult_matrix(10, -10)
    
    def test_single_row(self):
        assert gen_mult_matrix(1, 5) == [[1, 2, 3, 4, 5]]
        assert gen_mult_matrix(10, 10)[4] == [5, 10, 15, 20, 25, 30,
                                              35, 40, 45, 50]
        assert gen_mult_matrix(5, 3)[4] == [5, 10, 15]

    def test_entire_matrix(self):
        assert gen_mult_matrix(5, 5) == [[1, 2, 3, 4, 5],
                                         [2, 4, 6, 8, 10],
                                         [3, 6, 9, 12, 15],
                                         [4, 8, 12, 16, 20],
                                         [5, 10, 15, 20, 25]]
        assert gen_mult_matrix(3, 2) == [[1, 2], [2, 4], [3, 6]]


class TestPrintResults:
    def test_expected_return(self):
        assert print_results(gen_mult_matrix(5, 5)) == None
        assert print_results(gen_mult_matrix(3, 2)) == None
