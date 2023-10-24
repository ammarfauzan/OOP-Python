from datetime import date
 
class Person:
    # Initialize the attribute for the Person
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # a class method to create a
    # Person object by birth year.
    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a
    # Person is adult or not.
    @staticmethod
    def adult_checker(age):
        return age > 18

print(Person.adult_checker(16))

person1 = Person('Ammar', 27)
person2 = Person.from_birth_year('Hasan', 1997)

person1.name = 'Udin'
 
print(person1.age)
print(person2.age)


