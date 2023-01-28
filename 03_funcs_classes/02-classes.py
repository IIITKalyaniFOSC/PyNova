class Human():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def get_fullname(self):
        return self.firstname + " " + self.lastname

    def birth_year(self):
        return 2023 - self.age

# instantiate class
person1 = Human("Joe", "Doe", 28)
# using a class method
print(person1.get_fullname())
# using a class method
print(person1.birth_year())
