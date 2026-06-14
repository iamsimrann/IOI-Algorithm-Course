class Dog:

    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance methods
    def bark(self, sound):
        return "{} barks {}".format(self.name, sound)

    def run(self):
        return "{} is running around".format(self.name)

# instantiate the object
buddy = Dog("Buddy", 5)

# call instance methods
print(buddy.bark("'Woof Woof!'"))
print(buddy.run())