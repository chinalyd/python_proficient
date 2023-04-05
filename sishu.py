class Person:
    def __init__(self):
        self.__name = 'haha'
        self.age = 22
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.age
person = Person()
print(person.get_age())
print(person.get_name())
