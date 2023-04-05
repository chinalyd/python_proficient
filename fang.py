class SmplClass:
    def info(self):
        print('This is a class Smplclass!')
    def mycacl(self, x, y):
        return x + y
sc = SmplClass()
print('Call the function to the result:')
sc.info()
print('Call the function mycacl() to the reesult:')
print(sc.mycacl(3, 4))

