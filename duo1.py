class Car():
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.licheng_reading = 0
    def get_car_name(self):
        long_name = str(self.year) + ' '+ self.manufacturer + ' ' + self.model
        return long_name.title()
    def read_licheng(self):
        print('Current miles already driven: ' + str(self.licheng_reading) + 'KM!')
    def update_licheng(self, mileage):
        if mileage >= self.licheng_reading:
            self.licheng_reading = mileage
        else:
            print('This is not plug-in power!')
    def increment_licheng(self, miles):
        self.licheng_reading += miles
class Battery():
    def __init__(self, battery_size = 60):
        self.battery_size = battery_size
    def describe_battery(self):
        print('New lithium battery capacity ' + str(self.battery_size) + " KW/h!")
    def get_range(self):
        if self.battery_size == 60:
            range= 140
        elif self.battery_size == 85:
            range = 185
        message = "Attention: the remain power can run " + str(range)
        message += ' KM'
        print(message)
class ChadianCar(Car):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()
