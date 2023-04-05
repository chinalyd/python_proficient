info = "Address: "
def func_father(country):
    def func_son(area):
        city = "Beijing "
        print(info + country + city + area)
    city = "JiNan "
    func_son("FengTai Aera")
func_father("China ")

