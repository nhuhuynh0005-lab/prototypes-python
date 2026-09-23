def binary_representation_16bit_unsigned(v: int) -> str:
    """
    Assume `v` is in the range [0, 65535]. Return its binary representation as a string of
    length 16, where each character is either '0' or '1'.
    """
    return "0000000000000000"

def binary_representation_16bit_signed(v: int) -> str:
    """
    Assume `v` is in the range [-32768, 32767]. Return its binary representation as a string of
    length 16, where each character is either '0' or '1'. The negative values uses two's complement format.
    """
    return "0000000000000000"