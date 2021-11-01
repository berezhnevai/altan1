# ***Логические и условные операторы***

# операторы сравнения

z = 3
w = 2

# операция "равно"
# мы спрашиваем "значение z равно значению переменной w"
result = z == w

# операция "не равно"
result = z != w

# операция "меньше"
result = z < w 

# операция "больше"
result = z > w 

# операция "меньше либо равно"
result = z <= w 

# операция "больше либо равно"
result = z >= w 

# чистые логические операции

var_1 = True 
var_2 = False   

# оператор "НЕ" "NOT, инверсия"

result = not var_2 

# оператор "И" (AND, конъюнкция)
# возвращает значение true только 
# тогда когда оба переменных являются true

result = var_1 and var_2 

# оператор "ИЛИ" (OR, дизьюнкция)
# возвращает значение false только тогда 
# когда оба переменных являются false
result = var_1 or var_2 

# пример комбинации логических операторов
a = 5
b = 3
c = 3

result = ((a > b) and (b != c)) or (a == c)


# print(result) 


# Условные операторы

var = 10

# оператор IF 

# if var != 0:
#     print("Hello")

# if False
#   print("Hi")

if not var < 12:
    print("Hello")

# оператор ELSE - иначе
# var = 5

# if var > 0:
#     print("больше нуля")
# else:
#     print("не больше нуля")

# оператор ELIF 
# esle if
# var = 0

# if var > 0:
#     print("больше нуля")
# elif var < 0:
#     print("меньше нуля")
# else:
#     print("равно нулю")

var = 'C'

if var == 'A':
    res = "literal A"
elif var == 'a':
    res = "literal a"
elif var == 'B':
    res = "literal B"
elif var == 'C':
    res = "literal C"

# print(res)

# пример. кальулятор. 

num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

op = input("Введите символ операции: ")

if op == '+':
    res = num_1 + num_2
elif op == '-':
    res = num_1 - num_2
elif op == '*':
    res = num_1 * num_2
elif op == '/':
    res = num_1 / num_2
else:
    res = "символ операции некорректен! :("

print(f"результат = {res}")