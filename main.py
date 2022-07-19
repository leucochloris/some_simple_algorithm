import random

people = 100
members_inside_team = 5

a = []  # all members
n = []  # here should be massif`s

# generator of all members
for i in range(1, people, 1):
    a.append(i)

# generate a lot of empty massif`s
for i in range(0, int(people / members_inside_team), 1):
    n.append([])
# print(a, '\n', n)


while len(n[0]) != 5:
    n[0].append((random.choice(a)))

    while len(n[1]) != 5:
        n[1].append((random.choice(a)))

        while len(n[2]) != 5:
            n[2].append((random.choice(a)))

            while len(n[3]) != 5:
                n[3].append((random.choice(a)))

                while len(n[4]) != 5:
                    n[4].append((random.choice(a)))

print(n)
# random index of all members
# print("Сотрудник", a[random.choice(a)])
