import random

people = 101
members_inside_team = 5

a = []  # all members
n = []  # here should be massif`s

# generator of all members
for i in range(1, people):
    a.append(i)

# generate a lot of empty arrays
for i in range(0, int(people / members_inside_team)):
    n.append([])

# fill the array with data (we clear the sequence (array A) - so that the data does not repeat
for x, el_2 in enumerate(n):
    for j in range(members_inside_team):
        vrem = random.choice(a)
        el_2.append(vrem)
        a.remove(vrem)

# output every team
for eksl in n:
    print(eksl)