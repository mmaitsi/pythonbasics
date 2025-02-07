# objected oriented programming
class Cars:
    # constructor method
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    # a method function
    def describe_car(self):
        print(f"My dream car make: {self.make} "f"My dream car model: {self.model} "f"Manufacturer: {self.year}")

# create object or instances of a class
my_obj=Cars("Toyota","Lexus",2024)
my_obj.describe_car()
my_obj2=Cars("BMW","M3",2015)
my_obj2.describe_car()
my_obj3=Cars("Mercedes","c63",2020)
my_obj3.describe_car()
my_obj4=Cars("Porsche","911",2010)
my_obj4.describe_car()
my_obj5=Cars("Ford","Focus",2018)
my_obj5.describe_car()
