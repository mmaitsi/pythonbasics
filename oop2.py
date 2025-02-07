# class called fruits
# attributes name,colour,price
# implement a constructor method and a method function that prints my favourite fruit is this in colour and costs
# create 5 instances of that class
class Fruits:
    def __init__(self, name,color,price):
        self.name = name
        self.color = color
        self.price = price
    def describe_fruits(self):
        print(f"My favourite fruit is {self.name},",f"{self.color} in color",f"and costs {self.price}")
my_fruit = Fruits("apple","red",50)
my_fruit.describe_fruits()
my_fruit2 = Fruits("pineapple","yellow",100)
my_fruit2.describe_fruits()
my_fruit3 = Fruits("avocado","green",150)
my_fruit3.describe_fruits()
my_fruit4 = Fruits("grape","purple",200)
my_fruit4.describe_fruits()
my_fruit5 = Fruits("orange","orange",250)
my_fruit5.describe_fruits()


