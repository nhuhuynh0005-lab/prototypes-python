def binary_representation_16bit_unsigned(v: int) -> str:
    """
    Assume `v` is in the range [0, 65535]. Return its binary representation as a string of
    length 16, where each character is either '0' or '1'.
    """
    binary_list = []

    for _ in range(16):
        if v != 0:
            ind = v % 2
            devide_result = (v - ind) // 2
            v = devide_result
            binary_list.append(ind)
    a = "".join(map(str, binary_list))
    rev = a[::-1]
    return rev.rjust(16, "0")


def binary_representation_16bit_unsigned2(v: int) -> str:
    digits = [None] * 16
    for i in range(16):
        digit = v % 2
        v //= 2
        digits[15 - i] = str(digit)
    return "".join(digits)


def binary_representation_16bit_signed(v: int) -> str:
    """
    Assume `v` is in the range [-32768, 32767]. Return its binary representation as a string of
    length 16, where each character is either '0' or '1'. The negative values uses two's complement format.
    """
    return "0000000000000000"


if __name__ == "__main__":
    print(binary_representation_16bit_unsigned2(100))
