#!/usr/bin/python

# written: adamzs 06/20
# The global minimum is at (a, a^2)

import sys

from params import *

def rosenbrock(params):

	x, y = params

	a = 1.
	b = 100.

	f_val = (a - x)**2.0 + b*(y - x**2.)**2.

	return f_val

with open('results.out', 'w') as f:
	f.write('{:.60g}'.format(rosenbrock([x, y])))

