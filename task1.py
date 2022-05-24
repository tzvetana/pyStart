#Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print("Is the day a weekend?")
print("Enter the serial number of the day of the week")
daynum = int(input())
if 5 >= daynum >= 1 :
    print("no")
elif 7 >= daynum >= 6 :
    print("yes")
else:
    print("On this planet, it is customary to count weeks of seven days. Please enter the correct day number")