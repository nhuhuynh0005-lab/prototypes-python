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
        return '✅'

    return '❌'

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


def is_lower(pw):
    for a in pw:
        if a.islower():
            return True

print(f"{format_bool(is_lower(password))} Contains lower_case characters")


def is_upper(pw):
    for x in pw:
        if x.isupper():
            return True
        
print(f"{format_bool(is_upper(password))} Contains upper_case characters")


def is_digit(pw):
    for w in pw:
        if w.isdigit():
            return True

print(f"{format_bool(is_digit(password))} Contain numeric characters")

def is_special(pw):
    for p in pw:
        if not  p.islower() and not p.isupper() and not p.isdigit():
            return True
        
print(f"{format_bool(is_special(password))} Contains special characters")

