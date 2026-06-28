# def print_kwargs(**kwargs):
#    print('Keyword arguments:', kwargs)

# print_kwargs(wine="merlot", entree="mutton", dessert="macaroon")

# def print_data(data, *, start=0, end=100):
#     for value in (data[start:end]):
#         print(value)

# data = ['a','b','c','d','e','d']
# print_data(data)


# outside = ['one', 'fine', 'day']
# def mangle(arg):
#    arg[1] = 'terrible!'
# print(outside)
# mangle(outside)
# print(outside)

# def echo(anything):
#     """echoは、与えられた入力引数を返す。"""
#     return anything

# def print_if_true(thing, check):
#     """
#     第2引数が真なら、第1引数を表示する
#     処理内容:
#         1. 第2引数が真かどうかをチェックする。
#         2. 真なら第1引数を表示する。
#     """
#     if check:
#         print(thing)
# print(echo.__doc__)     

# def answer():
#     print(42)

# answer()

# def run_something(func):
#     func()
# run_something(answer)

# def add_args(arg1, arg2):
#     print(arg1 + arg2)

# add_args(1, 2)  

 
# def run_something_with_args(func, arg1, arg2):
#     func(arg1, arg2)

# run_something_with_args(add_args, 5, 9)



# def filter(arr, filterFn):
#     new_arr = []

#     for v in arr:
#         if filterFn(v):
#             new_arr.append(v)
    
#     return new_arr

# arr = [1, 2, 3, 4, 5]

# def is_even(v):
#     return v % 2 == 0

# def is_odd(v):
#     return v % 2 == 1

# print(filter(arr, is_even))
# print(filter(arr, is_odd))

# def sum_args(*args):
#    return sum(args)

# def run_with_positional_args(func, *args):
#     return func(*args)
# print(run_with_positional_args(sum_args, 1, 2, 3, 4))

# def outer(a, b):
#     def inner(c, d):
#         return c + d
#     return inner(a, b)

# print(outer(4, 7))

def knights2(saying):
    def inner2():
        return f"We are the knights who say: '{saying}"
    return inner2

a = knights2('Duck')
b = knights2('HAsenpfeffer')

print(a)
print(a())

def edit_story(words, func):
    for word in words:
        print(func(word))
stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word):   # 文にインパクトを与える
    return word.capitalize() + '!'
edit_story(stairs, enliven)
edit_story(stairs, lambda word: word.capitalize() + '!')


short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
     print('Need a position between 0 and', len(short_list) - 1, ' but got',
            position)

