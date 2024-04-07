# 1) create 3 functions "show1()","show2()" and "show3()"
# now define a function "caller" in such a way that it can accept any function as an argument and invoke the same.


def show1(a,b):
    print("from function show1():",b- a)

def show2(a,b):
    print(" from function show2():",a+b)

def show3(a,b):
    print("from show3:",a/b)

def caller(func):
    def release(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return release
var1 = caller(show2)
var1(10, 2)
var2 = caller(show3)
var2(5,7)
var3 = caller(show1)
var3(7,8)

# invoke caller function by passing show1,show2 and show3

# 2) define nested function and show how will you invoke it.



def outer_fun():
    print("This is the outer function.")

    def inner_fun():
        print("This is the inner function.")

    # Invoke the inner function
    inner_fun()

# Invoke the outer function
outer_fun()
