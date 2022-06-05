#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input("Enter a number, please:  "))
result = ' '
while number != 0:
    if number > 0:
        result = str(number % 2 ) + result
        number = number // 2
    
    elif number < 0:
        number = 0 - number
        result = str(number % 2 ) + result
        number = number // 2
    else:
        print("It's amazing, but 0 equals 0")
print(result)
