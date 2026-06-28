import sys

MIN_CHAR = 8


def is_long_enough(p: str) -> bool:
    """Return True if the password has at least MIN_CHAR characters."""
    return len(p) >= MIN_CHAR


def contain_upper(p: str) -> bool:
    """Return True if the password contains at least one upper-case letter."""
    for c in p:
        if c.isupper():
            return True
    return False


def contain_lower(p: str) -> bool:
    """Return True if the password contains at least one lower-case letter."""
    for c in p:
        if c.islower():
            return True
    return False


def contain_numeric(p: str) -> bool:
    """Return True if the password contains at least one numeric character."""
    for c in p:
        if c.isnumeric():
            return True
    return False


def contain_special(p: str) -> bool:
    """Return True if the password contains at least one special (non-alphanumeric) character."""
    for c in p:
        if not c.isalnum():
            return True
    return False


top_10_common_passwords = {
    "123456",
    "123456789",
    "111111",
    "password",
    "qwerty",
    "abc123",
    "12345678",
    "password1",
    "1234567",
    "123123",
}


def is_common(p: str) -> bool:
    """Return True if the password is in the top 10 most common passwords."""
    return p in top_10_common_passwords


def format_bool(v: bool) -> str:
    """Return a checkmark emoji for True and a cross emoji for False."""
    return "✅" if v else "❌"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 password_policy_checker.py <password>")
        sys.exit(1)

    password = sys.argv[1]
    print(f"{format_bool(is_long_enough(password))} Has 8 or more characters")
    print(f"{format_bool(contain_lower(password))} Contains lower-case characters")
    print(f"{format_bool(contain_upper(password))} Contains upper-case characters")
    print(f"{format_bool(contain_numeric(password))} Contains numeric characters")
    print(f"{format_bool(contain_special(password))} Contains special characters")
    print(f"{format_bool(not is_common(password))} Is not common")
