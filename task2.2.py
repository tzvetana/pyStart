#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

dict = {}
num = 0
n = int(input('Enter a number: ')) 
for i in range (1, n + 1):
    num = num + round((1+1/n)**n)
    dict[i] = num 
   
print(dict)





