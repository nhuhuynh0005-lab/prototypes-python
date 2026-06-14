# 1
e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}


# 2
print(e2f["walrus"])

# 3
f2e = {}
for x in e2f.items():
    f2e[x[1]] = x[0]
print(f2e)


# 4
for x in e2f.items():
    if x[1] == "chien":
        print(x[0])

# 5
name_set = e2f.keys()
print(name_set)

# 6
life = {
    "animal": {"cat": ["Henri", "grumpy", "Lucy"], "octopy": {}, "emus": {}},
    "plant": {},
    "other": {},
}


# 7.# 8
for k in life.items():
    if k[1] != {}:
        print(k[0])


# 9

for k in life.items():
    if k[0] == "animal":
        c = k[1]
        print(c["cat"])

# 10
squares = {}
for m in range(10):
    squares[m] = m * m
print(squares)

# 11
set_n = set()
for w in range(10):
    if w % 2 != 0:
        set_n.add(w)
print(set_n)

# 12
a_str = "optimist", "pessimist", "troll"
b_str = "The glass is half full", "The glass is half empty", "How did you get a glass?"
ab = dict(zip(a_str, b_str))
print(ab)

# 13
titles = ["Creature of Habit", "Crewel Fate", "Sharks On a Plane"]
plots = ["A nun turns into a monster", "A haunted yarn shop", "Check your exits"]

tp = dict(zip(titles, plots))
print(tp)
