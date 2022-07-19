import random

a = []
b = []

#generator of all members
for i in range(1, 101, 1):
    a.append(i)

# random index of all members
print(a[random.choice(a)])

# all members of team
print(a)