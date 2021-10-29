# -*- coding: utf-8 -*-
"""
Erster Punkt: P1 = (-1.1, 3.5)
Zweiter Punkt: P2 = (2.4, -0.7)
Für die Gerade y = mx + t durch P1 und P2 gilt:
m= -1.200 und t = 2.180
y = m * x + t
"""

import sys
import math
import random
def randomCoord():
    return (round(random.uniform(-10,10),1),round(random.uniform(-10,10),1))
p1 = randomCoord();
p2 = randomCoord();

print("Erster Punkt: P1 = (%.1f/%.1f)" % (p1[0],p1[1]))
print("Zweiter Punkt: P2 = (%.1f/%.1f)" % (p2[0],p2[1]))
m = (p1[1]-p2[1])/(p1[0]-p2[0])
t = (-1)*(p1[0]*m-p1[1])
print("y = %.3f * x + %.3f" % (m,t))

 