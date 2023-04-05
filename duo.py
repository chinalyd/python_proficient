class PrntOne:
    namea = 'PrntOne'
    def set_value(self, a):
        self.a = a
    def set_namea(self, namea):
        PrntOne.namea = namea
    def info(self):
        print('PrntOne: %s, %s'%(PrntOne.namea, self.a))
class PrntSecond:
    nameb = 'PrntSecond'
    def set_nameb(self, nameb):
        PrntSecond.nameb = nameb
    def info(self):
        print('PrntSecond: %s, %s'%(PrntSecond.nameb, self.a))
class Sub(PrntOne, PrntSecond):
    pass
class Sub2(PrntSecond, PrntOne):
    pass
class Sub3(PrntOne, PrntSecond):
    def info(self):
        PrntOne.info(self)
        PrntSecond.info(self)
print('Use the first subclass:')
sub = Sub()
sub.set_value('11111')

sub.info()
sub.set_nameb('22222')

sub.info()
print('Use the second subclass:')
sub2 = Sub2()
sub2.set_value('33333')
sub2.info()
sub2.set_nameb('44444')
sub2.info()
print('Use the third subclass:')
sub3 = Sub3()
sub3.set_value('55555')
sub3.info()
sub3.set_nameb('66666')
sub3.info()

