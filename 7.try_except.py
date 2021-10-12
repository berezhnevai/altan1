# *** Исключения (исключительные события, ситуации, ошибки)***

# Пример исключения при делении на ноль
# a = 100
# b = 0

# # отлов исключения
# try:
#     # потенциально аварийный код
#     c = a / b
#     print("все нормально:)")
# except:
#     # код, который должен сработать при исключении
#     print("что-то пошло не так :(")
#     c = 0


# print(c) 

# *** Обработка множества исключений***

# try:
#     a = int(input("Введите число: "))
#     result = 100 / a
# #  конкретные типы(классы) исключений
# except ZeroDivisionError:
#     print("на ноль делить нельзя!")
# except ValueError:
#     print("нужно ввести число")
# # общее исключение
# except Exception as error:
#     print(error)

# *** Конструкция "tr-except-finally" ***
# try:
#     a = int(input("Введите число: "))
#     result = 100 / a
#     print('Полет нормальный !:)')
# except ZeroDivisionError:
#     print("на ноль делить нельзя!:)")
#     result = 0
# finally:
#     print("Сработала finally")
#     result = 10 
 
# print(result)


# *** Кастомизированные ***
# try:
#     a = input("Введите символ: ")
#     if a == 'A':
#         raise Exception("Ошибка А")
#     elif a == 'B':
#         raise Exception("Ошибка Б")
#     elif a == 'С':
#         raise Exception("Ошибка C")
# except Exception as err:
#     print(err)


# *** Пример приближенный к реальности ***
# while True:
#     try:
#         a = int(input("Введите число: "))
#         c = 100 / a
#     except ZeroDivisionError:
#         print("на ноль делить нельзя")
#         continue
#     except ValueError:
#         print("это не число")
#         continue
#     print(f"Result:{c}")
#     break

#  *** Пример калькулятора***
from typing import final


def calculate(n1, n2, op):
    d = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    return d[op](n1, n2)
while True:
    # ввод данных
    cmd = input("Командуйте, сэр!: ")
    if cmd == "stop":
        print("Bye, bye!")
        break
    try:
        num_1 = int(input("Введите 1 число: "))
        num_2 = int(input("Введите 2 число: "))
        op = input("Введите символ операции: ")

        # обработка данных 
        result = calculate(num_1, num_2, op)

    except ZeroDivisionError:
        result = "на ноль делить нельзя"
        # continue
    except ValueError:
        result = "это не число"
        # continue
    finally:
        # вывод данных
        print(f"результат: {result}")

   