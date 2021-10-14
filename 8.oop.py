# ***Основы Объектно-ориентированного программирования***

# Объекты обладают свойствами и методами 
# Каждый объект принадлежит определенному классу (типу)

# класс = "чертеж" объекта. 
# объект = экземпляр (инстанс) класса.

# Создание (определение) класса 
# Название классов принято писать с заглавной буквы

class Cat:
    # метод-конструктор
    def __init__(self):
        # свойства (атрибуты, поля)
        self.name = None
        self.color = None
        

    # метод (атрибут-метод)
    def mur(self):
        print("Mur-mur!")
    
    def speech(self):
        print(f"Name: {self.name}, Color: {self.color}")
    
    # "Магический" метод (метод перезагрузки операторов),
    # который наделяет объект способностью функций
    def __call__(self, a, b):
        return a + b

# *Создание объектов (экземпляров класса) на базе класса Cat

cat_1 = Cat()
cat_2 = Cat()

# запись данных в свойства
cat_1.name = "Pushok"
cat_1.color = "White"

cat_2.name = "Juchka"
cat_2.color = "Black"

# чтение данных из свойств
# print(cat_1.name)
# print(cat_2.name)

# вызов метода

# cat_1.mur()
# cat_1.speech()
# cat_2.mur()
# cat_2.speech()


# благодаря методу __call__ объекты ведут себя как функции
result = cat_1(100, 20)
# print(result)


# ***Приницпы ООП***

# **Приницп наследования**

# создание родительского (предкового) класса
class Animal:
    def __init__(self, num_legs):
        self.legs = num_legs

    def move(self):
        print("Я двигаюсь!")

# создание дочерних классов

class Human(Animal):
    def __init__(self, num_legs, name):
        super().__init__(num_legs)
        self.name = name

    def speech (self):
        print(f"My name is {self.name}. Legs: {self.legs}")


class Cat_2(Animal):
    def __init__(self, legs, name, color):
        super().__init__(legs)
        self.name = name
        self.color = color 
    def speech (self):
        print(f"My name is {self.name}. Legs: {self.legs}, Color:{self.color}")

    def mur(self):
        print("Mur-mur!")

# создание объекта
bug = Animal(6)

man_1 = Human(2, "Petya")

woman_1 = Human(2, "Ira")

cat_1 = Cat_2(4, "Pushok", "White")


# вызовы методов

bug.move()
print(bug.legs)


man_1.speech()

woman_1.speech()

cat_1.speech()
