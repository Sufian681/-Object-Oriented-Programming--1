class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self. age = age

tom = Parrot("tom", 10)
jerry = Parrot("jerry", 15)

print("tom is a", tom.species)
print("jerry is also a", tom.species)
print("{} is {} years old".format( tom.name, tom.age))
print("{} is {} years old".format( jerry.name, jerry.age))

