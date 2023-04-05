class X_Property:
    class_name = "X_Property"
    def __init__(self, x=0):
        self.x = x
    def class_info(self):
        print('Class variable value: ',X_Property.class_name)
        print('Instance variable value: ',self.x)
    def chng(self, x):
        self.x = x
    def chng_cn(self, name):
        X_Property.class_name = name
aaa = X_Property()
bbb = X_Property()
print('Initialize two instance')
aaa.class_info()
bbb.class_info()
print('Modify instance variable')
print('Modify aaa instance variable')
aaa.chng(3)
aaa.class_info()
bbb.class_info()
bbb.chng(10)
aaa.class_info()
bbb.class_info()
print('Modify class variable')
print('Modify aaa class variable')
aaa.chng_cn('aaa')
aaa.class_info()
bbb.class_info()
print('Modify bbbclass variable')
bbb.chng_cn('bbb')
aaa.class_info()
