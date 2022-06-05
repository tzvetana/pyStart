#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("Enter the limit, please:  "))
factorial_list = []
composition = 1

for i in range(1, n+1):
    composition *= i
    factorial_list.append(composition)

print(f"The factorial of each of {n} numbers is  {factorial_list}")
