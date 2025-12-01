"""Core functionality for mypackage."""


def calculate(x, y):
    """Calculate the sum of two numbers.

    Args:
        x: First number
        y: Second number

    Returns:
        The sum of x and y
    """
    return x + y


def process_data(data):
    """Process a list of data.

    Args:
        data: List of items to process

    Returns:
        Processed data
    """
    return [item * 2 for item in data]
