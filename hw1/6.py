from cmath import sqrt
from math import pi, sqrt


figure_type = input('Choose a figure (circle, triangle, rectangle): ')
if figure_type == 'circle':
    radius = float(input('Enter a radius: '))
    print(pi * radius * radius)
elif figure_type == 'triangle':
    a, b, c = [float(num) for num in input('Enter three sides of a triangle: ').split()]
    p = (a + b + c) / 2
    print(sqrt(p * (p - a) * (p - b) * (p - c)))
elif figure_type == 'rectangle':
    a, b = [float(num) for num in input('Enter two sides of a rectangle: ').split()]
    print(a * b)
else:
    print('You must enter circle, triangle or rectangle')
