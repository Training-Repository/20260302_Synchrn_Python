__all__ = ['greet', 'greetName', 'greetInteractive']

def greet():
    print("Hi there!")

def greetName(name):
    greeting = "Hello"
    final_greeting = PrepGreeting(greeting, name)
    print(final_greeting)

def PrepGreeting(greeting, name):
    return greeting + " " + name + "!!"

def greetInteractive():
    name = input("Enter your name:")
    greeting = "Hey"
    final_greeting = PrepGreeting(greeting, name)
    print(final_greeting)

def Test():
    greet()
    greetName("Manish")
    greetInteractive()

# print(f"Greetings --> {__name__}")

if __name__ == '__main__':
    Test()
