#Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#from random import randint

start_list = [1, 2, 53, 4, 54, 62, 71, 84, 94]

print(f"The specified array {start_list}")

odd_list = start_list[:: 2]
print("The elements at odd positions in the original array")
print(odd_list)
sum = 0
for i in odd_list:
    sum = sum + i
print(f"Еhe sum of the list items in odd positions {sum}")