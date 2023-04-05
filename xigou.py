class NewClass(object):
    num_count = 0
    def __init__(self, name):
        self.name = name
        NewClass.num_count += 1
        print(name, NewClass.num_count)
    def __del__(self):
        NewClass.num_count -= 1
        print("Del", self.name, NewClass.num_count)
    def test():
        print("aa")
aa = NewClass("Hello")
bb = NewClass("World")
cc = NewClass("aaaa")
del aa
del bb
del cc
print("Over")

