#region Addition function
# def add(a, b):
#     sum = 0
#     if a ==0:
#         return b
#     elif b == 0:
#         return a
#     else:
#         sum  = a + b
#         return sum
    
# res = add(1, 2)
# print("Result ->", res)
# print(f"{res = }")

#endregion

#region Function Declaration (Define/Declare Higher vs. Define Earlier (Python))

# def Bar():
#     print("Enter Bar")
#     Baz()
#     print("Exit Bar")

# def Foo():
#     print("Enter Foo")
#     Bar()
#     print("Exit Foo")

# def Baz():
#     print("Enter Baz")
#     print("Executing...")
#     print("Exit Baz")

# def Main():
#     print("Enter Main")
#     Foo()
#     print("Exit Main")

# Main()
#endregion

#region Argument passing (Positional, Named, Default)
# def add(a:int, b:int)->int:
#     print(f"{a = }")
#     print(f"{b = }")
#     return a + b

# # print(f"{add(1, 2) = }")
# # print(f"{add(1.1, 2.2) = }")
# # print(f"{add("1", "2") = }")

# print(f"{add(1, 2) = }")        # Positional args
# print(f"{add(2, 1) = }")        # Positional args

# print(f"{add(b=2, a=1) = }")        # Named args


# def add(a, b=0, c=0):             # Default arg
#     print(f"{a = }")
#     print(f"{b = }")
#     print(f"{c = }")
#     return a + b + c

# print(f"{add(1, 2) = }")
# print(f"{add(1, 2, 3) = }")

#endregion

#region (un)packing
# a = 10
# b = 20

# a, b = 10, 20     # Assignment
# a, b = [10, 20]     # Unpacking + Assignment

# lst = [10, 20, 30]
# a, _,  b = lst

# lst = [10, 20, 30, 40, 50]
# # a, *rest,  b = lst    # Unpack lst --> Assign to LHS --> Pack into 'rest'
# a, *_,  b = lst         # Unpack lst --> Assign to LHS --> Pack into '_'

# print(f"{type(a) = }")
# # print(f"{type(rest) = }")
# print(f"{type(b) = }")
# print(a, b)
# # print(rest)


# def add(a, b):
#     return a+b

def add(a, b, *c):              # Definition (Receiving data from caller) --> apart from first 2 args, package the rest into 'c'
    print(f"{a = }")
    print(f"{b = }")
    print(f"{c = }")
    sum = a+b
    for val in c:
        sum += val
    return sum

lst = [10, 20, 30, 40, 50]
lst2 = [10, 20]

# print(add(lst[0], lst[1]))
# print(add(*lst))    # Call (sending data to 'add' method) --> Unpacking

print(add(*lst))
print(add(*lst2))

#endregion

