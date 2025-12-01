"""Tests for core module."""
import pytest
from mypackage.core import calculate, process_data


class TestCalculate:
    """Test cases for calculate function."""

    def test_calculate_positive_numbers(self):
        """Test calculation with positive numbers."""
        assert calculate(2, 3) == 5

    def test_calculate_negative_numbers(self):
        """Test calculation with negative numbers."""
        assert calculate(-1, -1) == -2

    def test_calculate_zero(self):
        """Test calculation with zero."""
        assert calculate(0, 5) == 5


class TestProcessData:
    """Test cases for process_data function."""

    def test_process_empty_list(self):
        """Test processing empty list."""
        assert process_data([]) == []

    def test_process_numbers(self):
        """Test processing list of numbers."""
        assert process_data([1, 2, 3]) == [2, 4, 6]

    def test_process_single_item(self):
        """Test processing single item."""
        assert process_data([5]) == [10]


@pytest.mark.parametrize("x,y,expected", [
    (1, 1, 2),
    (10, 20, 30),
    (-5, 5, 0),
    (0, 0, 0),
])
def test_calculate_parametrized(x, y, expected):
    """Parametrized tests for calculate function."""
    assert calculate(x, y) == expected
