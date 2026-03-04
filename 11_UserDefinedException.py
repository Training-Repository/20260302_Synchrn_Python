class InvalidAge(ValueError):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(self.message, self.code)

class IllegalAge(ValueError):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(self.message, self.code)

def CheckAge(age):
    if age < 0:
        raise InvalidAge("Age cannot be negative.", 1002)
    if age < 18:
        raise IllegalAge("Age must be 18 or older", 1005)
    print("Age is valid")

def Main():
    try:
        CheckAge(-5)
    except InvalidAge as ex:
        print(f"{ex!r} --> [{ex.message = }], [{ex.code = }]")
    except IllegalAge as ex:
        print(f"{ex!r} --> [{ex.message = }], [{ex.code = }]")

    try:
        CheckAge(16)
    except InvalidAge as ex:
        print(f"{ex!r} --> [{ex.message = }], [{ex.code = }]")
    except IllegalAge as ex:
        print(f"{ex!r} --> [{ex.message = }], [{ex.code = }]")

    try:
        CheckAge(21)
    except InvalidAge as ex:
        print(f"{ex!r} --> [{ex.message = }], [{ex.code = }]")
    except IllegalAge as ex:
        print(f"{ex!r} --> [{ex.message = }], [{ex.code = }]")


Main()