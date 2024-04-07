# 1)	accept a number and display its table.

def table(num):
    print(f"multiplication table for {num}")
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

num = int(input("enter the number: "))
table(num)

# ****************************************************************

# 2)	using switch ….case   display whether accepted character is vowel or not.

def vowel(char):
    vowels =['a','e','i','o','u']
    if char.lower in vowels :
        print(f'{char} is vowel')
    else:
        print(f'{char} is not vowel' )    

alpha =input("enter the character:")
vowel(alpha)        


# 3)	Display numbers  1 to 10 using  While loop

num = 1

while num <= 10:
    print(num)
    num += 1


# 4)  Display numbers from 3 to 30 except number 24  using while loop.
for i in range(3,30):
    if i == 24 :
        continue
    print(i)



# 5)accept marks from the user. Using if…….elif….  Else,  display whether result is  fail, pass, second class , first class, Distinction etc.

def result(marks):
    if marks < 0 or marks > 100:
        print("Invalid marks entered.")
    elif marks < 33:
        print("Result: Fail")
    elif marks <= 40:
        print("Result: Pass")
    elif marks <= 60:
        print("Result: Second Class")
    elif marks <= 80:
        print("Result: First Class")
    else:
        print("Result: Distinction")

# Example usage:
marks = float(input("Enter marks: "))
result(marks)


# 6) print the total of first 10 numbers.
sum = 0
for i in range(1,11):
    sum += i
    i += 1
print("Sum of first 10 number is:", sum)



# 7) accept numbers till user enters 0 and display the total of all the numbers entered.\
total = 0

while True:
    num = float(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    total += num

print("Total of all numbers entered:", total)






# 8) accept a character and display whether it is upper case or lower case or not an alphabet.
def charr(char):
    if char.isalpha:
        if char.isupper():
            print(f"{char} is uppercase")

        else:
            print(f"{char} is lowercase")

n = input("Enter the character:")
charr(n)                

# 9) display fibonicii series of 10 numbers
n=int(input("Enter the number: "))
x1=0
x2=1
s=[x1,x2]
for i in range(0,n-2):
    x=s[i]+s[i+1]
    s.append(x)
print(s)    


# 10) display prime numbers from 3 to 30

def prime_numbers(start, end):
    for num in range(start, end + 1):
        if num > 1 and all(num % i for i in range(2, num)):
            print(num, end=" ")

start = 3
end = 30

prime_numbers(start, end)


# 11) accept a number and display whether it is prime or not

def prime(num):
    if num < 2:
        return False
    return all(num % i for i in range(2, num))

# Accept a number from the user
num = int(input("Enter a number: "))

# Check if the number is prime
if prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
