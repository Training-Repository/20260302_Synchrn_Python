from random import randint



class Car:
    count = 0
    def __init__(self, make, model, year, color):
        self.serial = Car.genSerial()
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        Car.count += 1  # count = count + 1

    @staticmethod
    def genSerial():
        return randint(100, 999)

    def display(self):
        # print(f"{make}")
        print(f"{self.make}, {self.model}, {self.year}, {self.color}")

    def __str__(self):
        return f"{self.make}, {self.model}, {self.year}, {self.color}"

    def __repr__(self):
        return f"[{self.__class__.__name__}, Count: {self.count}, Serial: {self.serial}] {self.make}, {self.model}, {self.year}, {self.color}"
    
    @classmethod
    def car_count(cls):
        # print(cls)
        return Car.count


class Geared(Car):
    def __init__(self, make, model, year, color, gears):
        self.gears = gears
        super().__init__(make, model, year, color)

    def __str__(self):
        return super().__str__() + f", {self.gears}"

#---------------------------------------------------------------------
# Consumer code

def Test1():
    print(Car.car_count())
    c1 = Car("Honda", "Civic", 2026, "White")

    print(c1)
    # c1.display()


    # i1 = 10
    # print(i1)
    # print(str(i1))
    # print(i1.__str__())
    # print(i1.__repr__())

    print(repr(c1))

    c2 = Car("Toyota", "Camry", 2024, "Yellow")
    print(repr(c1))
    print(repr(c2))
    print(f"{c2!r}")
    print(c1.__class__)
    print(c1.__class__.__name__)

    print(c1.car_count())
    print(Car.car_count())

    print(Car.genSerial())


def Test2():
    c1 = Car("Honda", "Civic", 2026, "White")
    print(c1)

    gc1 = Geared("Toyota", "Camry", 2024, "Yellow", 5)
    print(gc1)

Test2()
