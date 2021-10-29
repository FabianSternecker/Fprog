# -*- coding: utf-8 -*-
"""
Umrechung Fahrenheit/Celsius
Usage: Umrechnung
5 * (Fahrenheit - 32) = 9 * Celsius
"""

convert= input("Enter c for Celsius or f for Fahrenheit\n")
value = float(input("Enter value\n"))
if convert=="c":
    r = 9/5*value + 32
elif convert == "f":
    r = (5*value-160)/9
print("Result:%.1f" % r)