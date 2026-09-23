import pytest
from binary import binary_representation_16bit_signed, binary_representation_16bit_unsigned


@pytest.mark.parametrize(
    "value,expected",
    [
        (0, "0000000000000000"),
        (255, "0000000011111111"),
        (65535, "1111111111111111"),
    ],
)
def test_binary_representation_16bit_unsigned(value, expected):
    assert binary_representation_16bit_unsigned(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
        (0, "0000000000000000"),
        (255, "0000000011111111"),
        (32767, "0111111111111111"),
        (-1, "1111111111111111"),
        (-256, "1111111100000000"),
        (-32768, "1000000000000000"),
    ],
)
def test_binary_representation_16bit_signed(value, expected):
    assert binary_representation_16bit_signed(value) == expected
