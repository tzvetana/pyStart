#Напишите программу, которая по заданному номеру четверти, 
#показывает диапазон возможных координат точек в этой четверти (x и y).

print("Enter a number of the quarter")
number = int(input())
if number == 1:
    print("The points in this quarter have coordinates in the range x>0 and y>0")
elif number == 2:
    print("The points in this quarter have coordinates in the range x<0 and y>0")
elif number == 3:
    print("The points in this quarter have coordinates in the range x<0 and y<0")
elif number == 4:
    print("The points in this quarter have coordinates in the range x>0 and y<0")
else:
    print("Please enter the correct number")

