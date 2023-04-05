class Wai:
    def __init__(self, x=0, y=0, color='black'):
        self.x = x
        self.y = y
        self.color = color
    def haijun(self, x, y):
        self.x = x
        self.y = y
        print('Torpedo...')
        self.info()
    def info(self):
        print('Locate object: (%d, %d)'%(self.x, self.y))
    def attack(self):
        print('Lunch! ')
class FlyWai(Wai):
    def attack(self):
        print('Intercept! ')
    def fly(self, x, y):
        print('Rocket Force...')
        self.x = x
        self.y = y
        self.info()
flyWai = FlyWai(color='red')
flyWai.haijun(100,200)
flyWai.fly(12, 15)
flyWai.attack()
