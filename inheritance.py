class Dad:
    def football(self):
        print("Dad likes watching football")
class Mum:
    def cooking(self):
        print("Mum likes cooking")
class Boy(Dad):
    def boy_age(self):
        print("I'm a 20 year old")
my_boy=Boy()
my_boy.football()
my_boy.boy_age()

class Girl(Mum):
    def singing(self):
        print("And I love singing")
my_girl = Girl()
my_girl.cooking()
my_girl.singing()