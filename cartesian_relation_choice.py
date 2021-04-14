'''return cartesian products according to specified conditions'''

__author__ = 'David Saah <dasorange.hope@gmail.com>'
__copyright__ = 'Copyright (c) 2020'


def cartesian_product(A, B, q):
    if q == 0:
        for x in A:
            for y in B:
                # declare relation function (sample)
                s = (1/x)-(1/y)

                # test to see if condition is satisfied
                if s == int(s):
                    continue
                else:
                    # prints cartesian products that satisfy the relation
                    print((x, y))

    if q == 1:
        for x in A:
            for y in B:
                # declare relation function (sample)
                s = (1/x)-(1/y)

                # test to see if condition is satisfied
                if s == int(s):
                    # prints cartesian products that satisfy the relation
                    print((x, y))
                else:
                    continue

# declare set variables here


# replace set variables with (A, B, q)
cartesian_product(A, B, q)
