import sys
from random import *
from datetime import datetime

seed(datetime.today().timestamp() + int(sys.argv[1]))


# could write this in any language but writing python is quick and I can do things like
# print('c' * 300000)



# CREATE A TEST SCRIPT BELOW HERE
# ---------------------------  EXAMPLE ------------------------------------- #

n = randint(1, 500)     # first argument is min, other is max, both inclusive
m = randint(1, 500)
mx = 1 << 31
print(n)
for i in range(n):
    print(randint(-mx, mx - 1), end=' ')
print()
print(m)
for i in range(m):
    print(randint(-mx, mx - 1), end=' ')
print()
