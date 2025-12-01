"""Integration tests for mypackage."""
from mypackage import calculate, process_data


def test_integration_workflow():
    """Test complete workflow."""
    data = [1, 2, 3]
    processed = process_data(data)
    result = calculate(processed[0], processed[1])
    assert result == 6


def test_version_exists():
    """Test that package has version."""
    import mypackage
    assert hasattr(mypackage, '__version__')
    assert isinstance(mypackage.__version__, str)
