# -*- coding: utf-8 -*-
"""
Ein Programm zur Berechnung von Zinsen
Usage: Zinsen Startkaptial Zinssatz Laufzeit
K0 = 1000.00, n = 5, p = 2.0 folgt K5 = 1104.08
Kn = K0 · (1 + p/100)^n
"""

import sys
import math
k0 = float(sys.argv[1])
p = float(sys.argv[2])
n = int(sys.argv[3])
kn = k0*math.pow(1+p/100,n)
                 
print(kn)