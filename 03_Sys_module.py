import sys

def demo_sys():
    print(f"Python version: {sys.version}")
    print(f"System PATH: {sys.path}")
    print(f"Arguments: {sys.argv}")
    if len(sys.argv) == 3:
        sum = int(sys.argv[1]) +  int(sys.argv[2])
        print(f"Sum: {sum}")
    


demo_sys()

