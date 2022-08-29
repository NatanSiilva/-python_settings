from .start import sum_number


def test_sum():
    """Testing sum"""
    result = sum_number(1, 2)
    assert result == 3, "Sum 1 + 2 should be 3"
