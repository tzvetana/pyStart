#Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print("Enter the X-axis coordinates")
x = int(input())
print("Enter the Y-axis coordinates")
y = int(input())
if x > 0 and y > 0:
    print("the point is in the 1 quarter")
if x < 0 and y > 0:
    print("the point is in the 2 quarter")
if x < 0 and y < 0:
    print("the point is in the 3 quarter")
if x > 0 and y < 0:
    print("the point is in the 4 quarter")