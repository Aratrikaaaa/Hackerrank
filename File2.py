class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def meow(self):
        print("meow meow")

c = Cat("Billie",23)
c.get_name()
c.get_age()

