'''calculates cartesian products of two sets'''

__author__ = 'David Saah <dasorange.hope@gmail.com>'
__copyright__ = 'Copyright (c) 2020'

from itertools import product
import time


def cartesian_product(A, B):
    for x in A:
        for y in B:
            print((x, y))


# declare sets here
A = {2, 3, 4, 5}
B = {6, 7, 8, 9}
# replace  set variable with (A, B)
tic1 = time.perf_counter()
cartesian_product(A, B)
toc1 = time.perf_counter()
print(f'{toc1-tic1:0.4f}')

print('\n')

tic2 = time.perf_counter()
c = product(A, B)
for x in c:
    print(x)
toc2 = time.perf_counter()
print(f'{toc2-tic2:0.4f}')
