#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


#while n>2:
    #n1, n2 = n2, n1 + n2
    #print(n2, end =' ')
    #n -= 1

n = int(input('Enter a number: '))

def get_fibonacci(n):
    fibonacci_list = []
    n1, n2 = 0, 1
    for i in range(0,n+1):
        fibonacci_list.append(n1)
        n1, n2 = n2, n1 + n2
    n1, n2 = 1, -1
    for i in range (n):
        fibonacci_list.insert(0, n1)
        n1, n2 = n2, n1 - n2
    return fibonacci_list
fibonacci_list = get_fibonacci(n)
print(get_fibonacci(n))
