# import os
# from random import randint
# def OpenFile():
#     fileName = input("Enter filename: ")

#     try:
#         if randint(0, 1):
#             raise ValueError("Invalid value entered!!")
        
#         if randint(0, 1):
#             raise ZeroDivisionError
        
#         if not os.path.exists(fileName):
#             print("File Not found!!")
#             # return "ERROR: FileNotFound"
#             raise FileNotFoundError("Where's the file?")
#     except Exception as ex:
#         print(f"EXCEPTION --> {ex!r}")
#         print("Releasing a few resources & performing local cleanup")
#         raise

#     with open(fileName, 'r') as file:
#         str1 = file. read()
#         print(f"Contents -> {str1}")

# def Consumer1():
#     OpenFile()
#     print("Done reading user file")    

# def Consumer2():
#     ret_code = OpenFile()
#     if "ERROR" in ret_code:
#         print("Some error faced while attempting to open file")
#     else:
#         print("Done reading user file")    

# def Consumer3():
#     try:
#         ret_code = OpenFile()
#         print("Releasing resource...")
#     except ZeroDivisionError as ex:
#         print(f"{ex!r}")
#     except FileNotFoundError as ex:
#         print(f"{ex!r}")
#     except Exception as ex:
#         print(f"EXCEPTION: {ex!r}")
#         print("Some error faced while attempting to open file")
#     else:
#         print("Done reading user file")
#     finally:
#         print("ALWAYS EXECUTES!")

#     print("Exiting the program now.")

# Consumer3()
 
###################################################################################

# class MyStack:
#     def __init__(self, size):
#         self.data = list()
#         self.size = size
#         self.count = -1

#     def Push(self, val):
#         if self.count < (self.size -1):
#             self.data.append(val)
#             self.count += 1
#             return True
#         return False
    
#     def Pop(self)->int:
#         if self.count >= 0:
#             return self.data.pop()
#         return -999

###################################################################################


def divide(a, b):
    assert b != 0, "Denominator cannot be zero."
    # raise AssertionError("...")
    return a/b

def consumer():
    n = 10
    d = 0

    try:
        print(divide(n, d))
    except Exception as ex:
        print(f"{ex!r}")

consumer()