import pandas as pd
import numpy as np
from typing import Optional


def create_df(a: int, b: int, random_seed: Optional[int] = None) -> pd.DataFrame:
    """
    Create a DataFrame with specified dimensions and random data.

    Args:
        a (int): Number of rows in the DataFrame
        b (int): Number of columns in the DataFrame
        random_seed (int, optional): Seed for random number generation for reproducibility

    Returns:
        pd.DataFrame: DataFrame with shape (a, b) containing random values

    Examples:
        >>> df = create_df(3, 4)
        >>> df.shape
        (3, 4)

        >>> df = create_df(2, 3, random_seed=42)
        >>> df
                    0          1          2
        0   0.374540  0.950714  0.731994
        1   0.598658  0.156019  0.155995
    """
    if a <= 0 or b <= 0:
        raise ValueError("Parameters 'a' and 'b' must be positive integers")

    # Set random seed if provided
    if random_seed is not None:
        np.random.seed(random_seed)

    # Create random data
    data = np.random.rand(a, b)

    # Create DataFrame
    df = pd.DataFrame(data)

    return df