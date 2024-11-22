def percent_to_string(value: float) -> str:
    """Convert a decimal value to a percentage string.
    
    Args:
        value: A decimal value from 0.0 to 1.0. 
    
    Returns:
        A string representation of the percentage.
    """

    if type(value) is not float:
        raise TypeError("Value must be a float.")

    if value < 0 or value > 1:
        raise ValueError("Value must be between 0.0 and 1.0.")
    
    return f"{round(value * 100)}%"

print(percent_to_string("hello"))