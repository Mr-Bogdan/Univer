class MyTetsClass:
    num_of_users = 0
    age_in_2016 = -5

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.fullinfo = 'My name ' + self.name + ', age ' + '.'
        MyTetsClass.num_of_users += 1

    def about_me(self):
        return self.fullinfo

    def what_age_in_2016(self):
        self.age = self.age + self.age_in_2016
        return self.age

    def __repr__(self):
        return 'Info: {}, {}'.format(self.name, self.age)

    def __str__(self):
        return '{} - {}'.format(self.age, self.what_age_in_2016())

    def __add__(self, other):
        return self.age + other.age

    def __len__(self):
        return len(self.name)


info = MyTetsClass("Bogdan", 20)
info1 = MyTetsClass("Max", 12)
info2 = MyTetsClass("Taras", 29)

print(repr(info))
print(str(info2))

print(info1 + info2)

print(len(info1))
