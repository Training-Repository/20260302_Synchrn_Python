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

# def add(a, b, *c):              # Definition (Receiving data from caller) --> apart from first 2 args, package the rest into 'c'
#     print(f"{a = }")
#     print(f"{b = }")
#     print(f"{c = }")
#     sum = a+b
#     for val in c:
#         sum += val
#     return sum

# lst = [10, 20, 30, 40, 50]
# lst2 = [10, 20]

# # print(add(lst[0], lst[1]))
# # print(add(*lst))    # Call (sending data to 'add' method) --> Unpacking

# print(add(*lst))
# print(add(*lst2))


# def Words2Sentence(*words):                     # Variable arg list
#     print(f"Received {len(words)} words.")
#     s1 = ""
#     for w in words:
#         s1 += w + " "
#     s1 += "."
#     return s1

# print(Words2Sentence("This", "is", "a", "test"))


# def PrintEmp(ceo, cto, **others):           # Keyworded Variable arguments
#     print(f"{ceo = }")
#     print(f"{cto = }")
#     # print(f"{others = }")
#     for pos, person in others.items():
#         print(f"{pos} = '{person}'")

# PrintEmp("Manish", "Abhijeet", cfo="Rakesh", hr="Vinay")


# Sepcial args
# / - Anything to the left HAS to be positional
# * - Anything to the right HAS to be keyworded/named
def Func(a, b, /, c, d, *, e, f):
    print(f"{a = }")
    print(f"{b = }")
    print(f"{c = }")
    print(f"{d = }")
    print(f"{e = }")
    print(f"{f = }")

# Func(1, 2, 3, 4, 5, 6)
Func(1, 2, 3, d=4, e=5, f=6)
Func(1, 2, 3, 4, e=5, f=6)
# Func(1, 2, 3, 4, 5, f=6)  # <-- ERROR

#endregion

