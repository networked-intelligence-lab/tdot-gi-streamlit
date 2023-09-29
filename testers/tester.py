
class Person():
    def __init__(self, name, age):
        self.name = name
        if age > 100:
            raise Exception("Age is too high")
        else:
            self.age = age

    def birthday(self):
        self.age += 1
        return self.age