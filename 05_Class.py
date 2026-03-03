class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display(self):
        print(f"{self.make}, {self.model}, {self.year}, {self.color}")

    def __str__(self):
        return f"{self.make}, {self.model}, {self.year}, {self.color}"

    def __repr__(self):
        return f"[{self.__class__.__name__}] {self.make}, {self.model}, {self.year}, {self.color}"

c1 = Car("Honda", "Civic", 2026, "White")

print(c1)
# c1.display()


# i1 = 10
# print(i1)
# print(str(i1))
# print(i1.__str__())
# print(i1.__repr__())
