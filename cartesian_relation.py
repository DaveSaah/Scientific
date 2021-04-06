'''returns cartesian products with condition of satisfied relation'''

__author__ = 'David Saah <dasorange.hope@gmail.com>'
__copyright__ = 'Copyright (c) 2020'

def cartesian_product(A, B):
	for x in A:
		for y in B:
			
			#declare relation function (sample)
			s =  (1/x)-(1/y)
			
			#test to see if condition is satisfied
			if s == int(s):
				p = True
			else:
				p = False
			
			#outputs cartesian product with condition
			print((x,y), p)

#declare set variables here

#replace set variables with (A, B)
cartesian_product(A, B)