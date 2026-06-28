import sys

password = sys.argv[1]

# if len(password) >= 8:
#     print("✅ Has 8 or more characters")
# else:
#     print("❌ Has 8 or more characters")


def is_long_enough(pw):
    return len(pw) >= 8


# helper


def format_bool(v):
    if v:
        return "✅"

    return "❌"


print(f"{format_bool(is_long_enough(password))} Has 8 or more characters")

# for s in password:
#     if s.islower():
#         print("✅ Contains lower-case characters")
#         break
# else:
#     print("❌ Contains lower-case characters")

# contain_lower_case = False
# for c in password:
#     if c.islower():
#         contain_lower_case = True
#         break

# if contain_lower_case:
#     print("✅ Contains lower-case characters")
# else:
#     print("❌ Contains lower-case characters")


def has_lower(pw):
    for a in pw:
        if a.islower():
            return True
    return False


print(f"{format_bool(has_lower(password))} Contains lower_case characters")


def has_upper(pw):
    for x in pw:
        if x.isupper():
            return True
    return False


print(f"{format_bool(has_upper(password))} Contains upper_case characters")


def has_digit(pw):
    for w in pw:
        if w.isdigit():
            return True
    return False


print(f"{format_bool(has_digit(password))} Contain numeric characters")


def has_special(pw):
    for p in pw:
        # if not p.islower() and not p.isupper() and not p.isdigit():
        if not p.isalnum():
            return True
    return False


print(f"{format_bool(has_special(password))} Contains special characters")

common_passwords = {
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


def is_not_common_password(pw):
    return pw not in common_passwords


print(f"{format_bool(is_not_common_password(password))} Is not common")
