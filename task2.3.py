#Реализуйте алгоритм перемешивания списка.


import random

start_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print (f"The original list is : {start_list}")

for i in range(len(start_list)-1, 0, -1):
    j = random.randint(0, i + 1) 
    start_list[i], start_list[j] = start_list[j], start_list[i] 

print (start_list)
