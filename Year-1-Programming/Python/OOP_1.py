class Dog:
    species = "Canis Familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

miles = Dog("Miles", 4)
buddy = Dog("Buddy", 9)

miles.age
buddy.name