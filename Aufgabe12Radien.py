from math import *


def umfangKreis(radius):
    return pi * radius * 2

def flaecheKreis(radius):
    return pi * radius ** 2

def summeUmfangKreis(radiusliste):
    return sum(map(umfangKreis, radiusliste))


def summeflaecheKreis(radiusliste):
    return sum(map(flaecheKreis, radiusliste))


radii = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(summeUmfangKreis(radii))
radii = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(summeflaecheKreis(radii))
