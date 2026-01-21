import numpy


def numpy_array(a: int, b: int) -> numpy.array:
    """
    Create numpy array
    Args:
        a (int): 1st arg
        b (int): 2nd arg
    Returns:
        numpy array
    """
    return numpy.array([a, b])

if __name__ == "__main__":
    print(numpy_array(1, 2))
