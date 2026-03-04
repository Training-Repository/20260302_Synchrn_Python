def Outer():
    # var = 3         # External
    def Fn1():
        # var = 1   # Local
        print(var)
        # var = 2   # ERROR
    
    # var = 4       # External
    return Fn1

var = 5

fn = Outer()
fn()