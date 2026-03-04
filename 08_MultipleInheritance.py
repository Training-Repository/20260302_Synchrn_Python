class Base:
    def __init__(self):
        print("Initialising Base...")
        # super().__init__()

    def display(self):
        print("Base")
        # super().display()

class A(Base):
    def __init__(self):
        print("Initialising A...")
        super().__init__()

    def display(self):
        print("A")
        super().display()

class B(Base):
    def __init__(self):
        print("Initialising B...")
        super().__init__()

    def display(self):
        print("B")
        super().display()

class C(A, B):
    def __init__(self):
        print("Initialising C...")
        super().__init__()

    def display(self):
        print("C")
        super().display()


#-------------------------------

c1 = C()
c1.display()


# Look up MRO (Method Resoution Order) mechanism for further details
# Properties (Getter, Setter)
# Abstract Classes
