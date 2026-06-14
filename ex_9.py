# 1
def good():
    return ["Harry", "Ron", "Hermione"]


print(good())


# 2
def get_odds():
    for x in range(10):
        if x % 2 != 0:
            yield x


count = 0
for n in get_odds():
    count += 1
    if count == 3:
        print(n)


# 3
def test(func):

    def new_function():
        print("start")

        func()

        print("end")

    return new_function


# 4
class OopsException(Exception):
    pass


try:
    raise OopsException
except OopsException:
    print("Caught an oops")
