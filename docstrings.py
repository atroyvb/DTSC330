import pandas as pd


def add(a: int | float, b: int | float) -> int | float:
    """Add to numbers together

    Args:
        a (int | float): number 1
        b (int | float): number 2

    Returns:
        int | float: output of addition of numbers 1 and 2
    """
    return a + b


def create_new_dataframe() -> pd.DataFrame:
    """Create a new dataframe with dummy data

    Returns:
        pd.DataFrame: dataframe containing dummy data
    """
    return pd.DataFrame([[1, 2,3 ]], columns=['test', 'random', 'name'])