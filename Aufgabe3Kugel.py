# -*- coding: utf-8 -*-
"""
O=4⋅π⋅r2
V=4/3⋅π⋅r3
"""

import sys
import math
radius = float(input("Enter radius\n"))
print("Volume: "+ str(radius**3*(4/3)*math.pi)+ "\n")
print("surface area: " + str(radius**2*4*math.pi) + "\n")
 