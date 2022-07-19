import random

people = 100
count_team = 20

a = []  # all members
n = []  # here should be massif`s

# generator of all members
for i in range(1, people, 1):
    a.append(i)

# generate a lot of empty massif`s
for i in range(0, int(people / count_team), 1):
    n.append([])
# print(a, '\n', n)


while len(n[0]) !=5:
    n[0].append((random.choice(a)))

print(n)

# random index of all members
# print("Сотрудник", a[random.choice(a)])