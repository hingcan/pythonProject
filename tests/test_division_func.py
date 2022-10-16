from my_funcs.utils import division
import pytest

@pytest.mark.parametrize("a, b, exp_result", [(22, 2, 11),
                                              (22, 1, 22),
                                              (6, 6, 1),
                                              (22, -2, -11),
                                              (10, 4, 2.5)])
def test_division_good(a, b, exp_result):
    assert division(a, b) == exp_result

@pytest.mark.parametrize("exp_exception, divisionable, divider", [(ZeroDivisionError, 10, 0),
                                                    (TypeError, 20, "0")])

def test_division_zero(exp_exception, divisionable, divider):
    with pytest.raises(exp_exception):
        division(divisionable, divider)
