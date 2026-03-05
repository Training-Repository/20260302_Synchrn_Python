# import greeting

# greeting.greet()
# greeting.greetName("Rakesh")
# print(f"Consumer --> {__name__}")

# from greeting import greet, greetName

# greet()
# greetName("Vijay")


def greet():
    print("Welcome to the training")

# from greeting import greet as grt

# greet()
# grt()


#-------------------------------------------

from greeting import *
from greeting import PrepGreeting, Test

greet()
greetName("John")
PrepGreeting("Hi", "Tim")
Test()

# def Fn1():
#     print("Inside Fn1()")
#     # from greeting import greet, greetName
#     # import greeting

#     # greeting.greet()
#     # greet()

#     # # print(f"{globals() = }")
#     # globals()['greet']()

#     #--------------------------------

    




#     print("Exiting Fn1()")

# Fn1()