class Site:
    def __init__(self, name, url):
        self.name = name
        self.__url = url
    def who(self):
        print('name :',self.name)
        print('url:',self.__url)
    def __foo(self):
        print("This is a private function.")
    def foo(self):
        print("This is a public function.")
        self.__foo()
x = Site('runoob', 'www.topper.net')
x.who()
x.foo()

