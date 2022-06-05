#Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

start_list = [1, 2, 53, 4, 54, 62, 71, 84, 94]
example_list = [2, 3, 4, 5, 6]

def pairs_multiply(list):
    results = []
    while len(list) > 1:
        results.append(list[0] * list[-1])
        del list[0] 
        del list[-1] 
    if len(list) ==1: results.append(list[0] **2)       
    return results

print(start_list)
print(pairs_multiply(start_list))

print(example_list)
print(pairs_multiply(example_list))