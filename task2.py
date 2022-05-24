#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print("¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z")
x = int(input("x"))
y = int(input("Y"))
z = int(input("Z"))

print("¬(X ⋁ Y ⋁ Z)")
if x == 0 or y == 0 or z == 0:
    disjunction = 1
elif x == 0 and y == 0 and z == 0:
    disjunction = 0
elif x == 1 and y == 1 and z == 1:
    disjunction = 1
if  disjunction == 0:
    resultdenial = True
else:
    resultdenial = False
print(resultdenial)

print("¬X ⋀ ¬Y ⋀ ¬Z")
if x == 0 and y == 0 and z == 0:
    conjunction = True
else:
    conjunction = False
print(conjunction)

if resultdenial == False and conjunction == False:
    result = True
elif  resultdenial == True and conjunction == True:
    result = True
else:
    result = False
print(result)

