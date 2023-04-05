class Jing:
    def __init__(self, x=0):
        self.x = x
    @staticmethod
    def static_method():
        print('Call the static method.')
    @classmethod
    def class_method(cls):
        print('Class the class method.')
Jing.static_method()
Jing.class_method()
dm = Jing()
dm.static_method()
dm.class_method()

