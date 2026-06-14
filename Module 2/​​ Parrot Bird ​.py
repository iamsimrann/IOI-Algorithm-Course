class Dog:

    # class attribute
    species = "mammal"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Dog class
buddy = Dog("Buddy", 5)
maxx = Dog("Max", 8)

# access the class attributes
print("Buddy is a {}".format(buddy.species))
print("Max is also a {}".format(maxx.species))

# access the instance attributes
print("{} is {} years old".format(buddy.name, buddy.age))
print("{} is {} years old".format(maxx.name, maxx.age))