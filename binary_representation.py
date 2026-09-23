def binary_representation_unsigned(v: int) -> str:
    """
    Assume `v` is in range [0, 65535]. Display its 16-bit binary representation.
    """
    binary_list = []

    for _ in range(16):
        if v != 0:
            ind = (v % 2)
            devide_result = (v - ind) // 2
            v = devide_result
            binary_list.append(ind)
        a = "".join(map(str, binary_list))
        rev = a[::-1]
    return rev.rjust(16, "0")


if __name__ == "__main__":
    for v in [15]:
        print(f"v={v}, binary={binary_representation_unsigned(v)}")
