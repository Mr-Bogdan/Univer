# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

car1 = Vehicle()
car1.name = "Ferrari"
car1.color = "red"
car1.kind = "convertible"
car1.value = 122000.00

car2 = Vehicle()
car2.name = "Tesla"
car2.color = "white"
car2.kind = "sedan"
car2.value = 34000.00
# test code
print(car1.description())
print(car2.description())