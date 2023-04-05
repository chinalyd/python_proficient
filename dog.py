class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def wang(self):
        print(self.name.title() +" wang wang")
    def shen(self):
        print(self.name.title() + " shen tongue")
d = Dog("PI", 12)
d.wang()
d.shen()
