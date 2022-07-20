import random

people = 101
members_inside_team = 5

a = []  # all members
n = []  # here should be massif`s

# generator of all members
for i in range(1, people):
    a.append(i)

# generate a lot of empty massif`s
for i in range(0, int(people / members_inside_team)):
    n.append([])
# print(a, '\n', n)


# while len(n[:]) != 5:
#     n[:].append((random.choice(a)))


for x, el_2 in enumerate(n):
    for j in range(members_inside_team):
        vrem = random.choice(a)
        el_2.append(vrem)
        a.remove(vrem)

for eksl in n:
    print(eksl)
