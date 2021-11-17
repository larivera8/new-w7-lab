#luis rivera
#11/14/21

#problem 6

class car:
    def __init__(self, model, year, color, manufacturer, type):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return self.model + ' ' + str(self.year) + self.manufacturer + ' '+self .type + ' ' +
         self.color

    car1 = car("Nissan", "GT-R", "Sports", 2012, "Blue")
    car2 = car("Toyota", "Corolla", "Sedan", 2020, "Black")

    print(car1.get_color())
    print(car1.get_model())
    print(car2.get_color())
    print(car2.get_model())
    print(car1.fullspecs())
    print(car2.fullspecs())
