class Person:
    def __init__(self, name,age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        print(self.__age)

    @age.setter
    def age(self, age):
        self.__age = age