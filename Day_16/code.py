class ninja:

    # class attribute
    species = "ninja"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


blu = ninja("Naruto", 20)
woo = ninja("Kakashi", 32)

print("Naruto is a {}".format(blu.__class__.species))
print("Kakashi is also a {}".format(woo.__class__.species))

print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))