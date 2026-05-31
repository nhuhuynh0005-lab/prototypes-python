guess_me = 7
number = 3

while True:
    if number == guess_me:
        print("found it!")
        break

    if number > guess_me:
        print("oops")
        break

    print("too low!")
    number += 1
