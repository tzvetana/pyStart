#Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

print("Enter the coordinates of the first point")
print("Enter the X-axis coordinates")
xa = int(input())
print("Enter the Y-axis coordinates")
ya = int(input())

print("Enter the coordinates of the second point")
print("Enter the X-axis coordinates")
xb = int(input())
print("Enter the Y-axis coordinates")
yb = int(input())

if xa == 0 and ya == 0:
    length = math.sqrt(xb**2 + yb**2)
    print(f"Thr distance between points is {length}")
elif xb == 0 and yb == 0:
    length = math.sqrt(xa**2 + ya**2)
    print(f"Thr distance between points is {length}")
else:
    length = math.sqrt((xa - xb)**2 + (ya - yb)**2)
    print(f"Thr distance between points is {length}")