# Mini Project: Password Policy Checker

**Topics:** variables · conditionals · loops · strings · sets · functions

## Overview

Build a CLI tool that checks whether a password meets all of the following rules:

1. At least 8 characters long
2. Contains at least one lower-case letter
3. Contains at least one upper-case letter
4. Contains at least one numeric digit (0–9)
5. Contains at least one special character (not a letter or digit)
6. Is not one of the 10 most common passwords

## Sample Output

```
python3 password_policy_checker/main.py Helloworld1!
✅ Has 8 or more characters
✅ Contains lower-case characters
✅ Contains upper-case characters
✅ Contains numeric characters
✅ Contains special characters
✅ Is not common

python3 password_policy_checker/main.py password
✅ Has 8 or more characters
✅ Contains lower-case characters
❌ Contains upper-case characters
❌ Contains numeric characters
❌ Contains special characters
❌ Is not common
```

## Milestones

### 1. Accept a CLI argument

Read the password as the first command line argument and print it.

**Sample output**

```
python3 password_policy_checker/main.py hello
hello
```

### 2. Rule 1 — Length

Print whether the password is at least 8 characters long.

**Sample output**

```
python3 password_policy_checker/main.py longpassword
✅ Has 8 or more characters

python3 password_policy_checker/main.py hi
❌ Has 8 or more characters
```

### 3. Rule 2 — Lower-case

Print whether the password contains at least one lower-case letter.

**Sample output**

```
python3 password_policy_checker/main.py helloworld
✅ Has 8 or more characters
✅ Contains lower-case characters

python3 password_policy_checker/main.py HELLOWORLD
✅ Has 8 or more characters
❌ Contains lower-case characters
```

### 4. Rule 3 — Upper-case

Print whether the password contains at least one upper-case letter.

**Sample output**

```
python3 password_policy_checker/main.py Helloworld
✅ Has 8 or more characters
✅ Contains lower-case characters
✅ Contains upper-case characters

python3 password_policy_checker/main.py helloworld
✅ Has 8 or more characters
✅ Contains lower-case characters
❌ Contains upper-case characters
```

### 5. Rule 4 — Numeric

Print whether the password contains at least one digit.

**Sample output**

```
python3 password_policy_checker/main.py Helloworld1
✅ Has 8 or more characters
✅ Contains lower-case characters
✅ Contains upper-case characters
✅ Contains numeric characters

python3 password_policy_checker/main.py Helloworld
✅ Has 8 or more characters
✅ Contains lower-case characters
✅ Contains upper-case characters
❌ Contains numeric characters
```

### 6. Rule 5 — Special character

Print whether the password contains at least one special character (anything that is not a letter or digit).

**Sample output**

```
python3 password_policy_checker/main.py Helloworld1!
✅ Has 8 or more characters
✅ Contains lower-case characters
✅ Contains upper-case characters
✅ Contains numeric characters
✅ Contains special characters

python3 password_policy_checker/main.py Helloworld1
✅ Has 8 or more characters
✅ Contains lower-case characters
✅ Contains upper-case characters
✅ Contains numeric characters
❌ Contains special characters
```

### 7. Rule 6 — Common passwords

Print whether the password is absent from the list of 10 most common passwords.

The 10 most common passwords are:

```
123456
123456789
111111
password
qwerty
abc123
12345678
password1
1234567
123123
```

**Sample output**

```
python3 password_policy_checker/main.py Helloworld1!
✅ Has 8 or more characters
✅ Contains lower-case characters
✅ Contains upper-case characters
✅ Contains numeric characters
✅ Contains special characters
✅ Is not common

python3 password_policy_checker/main.py password
✅ Has 8 or more characters
✅ Contains lower-case characters
❌ Contains upper-case characters
❌ Contains numeric characters
❌ Contains special characters
❌ Is not common
```

## Hints

- You can loop over the characters of a string with `for c in p:`.
- Python sets are a good fit for checking membership in the common-password blocklist.
