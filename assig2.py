
# 1) define 3 functions "add()","modify()" and "delete()" with just a print message.
# now accept input from user as a number. if the number entered is 1, call "add()"
# if it is 2, call "modify()" if it is 3, call "delete()" [ hint: use "match... case" ]

def add():
    print("from add()")

def modify():
    print("from modify()")

def delete():
    print("from delete()")

def main(): 
    n = int(input("Enter the number:"))
    match n:
        case 1:
            add()
        case 2 :
            modify()
        case 3:
            delete()
if __name__ == 'main':
    main()

       

# 2) define a function which accepts a number and return its square.
def square(n):
    return n ** 2

result = square(5)
print(result)



# 3) define a function which accepts character,int,string and display them.

def display(char, int, string):
    """ this fucntion accepts character ,int, string as input"""
    print("Charater",char)
    print("int",int)
    print("String",string)

display("A", 20,'HELLO')    


# 4) define "myfun1()" with a print statement. now define "myfun2()" which should invoke "myfun1()" function. 
# invoke myfun2()
def myfun1():
    print('myfun1')
def myfun2():
    print('myfun2')
    myfun1()
myfun2()    


# 5) define a function to accept a number. This function should return 1 if a number passed is more than 0
# return -1 if a number passed is less than 0 , else it should return 0.
def number(n):
    if n > 0:
        return 1
    elif n < 0 :
        return -1
    else:
        return 0
print(number(5))
print(number(-1))
print(number(0))    


# 6) define a function which accepts a character and return toggle of it.

def toogle_case(character):
    if character.isupper():
        return character.lower()
    elif character.islower():
        return character.upper()
    else:
        return character
    
print(toogle_case("A"))   
print(toogle_case('b'))


# 7) define a function which accepts a string , toggle and return it.
# 	[ hint :  use "swapcase()" function of string ]

def toggle_string(n):

    return n.swapcase() 

# Example usage:
result = "Hello, World!"
toogle_result = toggle_string(result)
print("Original String:", result)
print("Toggled String:", toogle_result)


# 8) write a function to accept minimum 3 characters and maximum 5 characters. 
# 	[ use default arguments method ]

def validate_string(s, min_length=3, max_length=5):
    if min_length <= len(s) <= max_length:
        return True
    else:
        return False

# Test cases
print(validate_string("abc"))  # True
print(validate_string("abcd"))  # True
print(validate_string("abcde")) # True
print(validate_string("abcdef")) # False
print(validate_string("ab"))    # False



# 9) define a function in such a way that it can accept n number of values and print their sum.


def summ(*args):
    total = sum(args)
    print("Sum of integer", total)
summ(1,2,3)
summ(5.5,4,3)    
