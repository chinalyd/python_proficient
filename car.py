class Car():
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.licheng_reading = 0
    def get_car_name(self):
        long_name = str(self.year) + ' '+ self.manufacturer + ' '+ self.model
        return long_name.title()
    def read_licheng(self):
        print('Current miles traveled ' + str(self.licheng_reading) + ' KM!')
    def update_licheng(self, mileage):
        if mileage >= self.licheng_reading:
            self.licheng_reading = mileage
        else:
            print('This is not plug-in power')
    def increment_licheng(self, miles):
        self.licheng_reading += miles
