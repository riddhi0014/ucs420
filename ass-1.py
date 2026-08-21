
#Assignment 1.1
print("Hello World")
name="Riddhi Jain"

for i in range(3):
  print(name)

#Assignment 1.2
a=5
b=14
print(a+b)

#Assignment 1.3
str1="Hello"
str2="Everyone"
num=2
str3=str1+" "+str2
print(str3)
print(str1,"+",str2, "->", str3)

#Assignment 2.1
a=100
b=200
c=300
result=a+b+c
print(f"The sum of a,b,c is : {result}")

#Assignment 2.2
str1="You"
str2="are"
str3="awesome"

str=str1+" "+str2+" "+str3
print(str)

# Different types of Inputs
name=input("Enter your name: ")  
print(name)

age=input("Enter your age: ")
print(age)
print(type(age))

age=int(input("Enter your age: "))
print(age)
print(type(age))

#Inputting two numbers
a,b =map(int,input().split())
print(a,b)
print(a+b)

#Inputting an array
n=int(input())
arr=list(map(int,input().split()))
print(arr)
print(type(arr))

#table of 5
for i in range(1,11):  #1 is inclusive, 11 is exclusive.
  print(i*5)


#Inputting a number and then applying some operations
n=int(input("Enter a number: "))

for i in range(1,n+1): #sum of 1 to n numbers
  print(i)

for i in range(1,11):
  print(n, "*",i,"=", n*i)


sum=0
for i in range(1,11):
  sum+=i
print(sum)


#Ranges
print(list(range(10)))
print(list(range(1,10)))
print(list(range(1,20,2)))
print(list(range(-10,-20,2)))
print(list(range(-10,-20,-2)))




#5

#5.1 Input two numbers from user and compare them
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a>b:
  print(a, ">", b)
elif a<b:
  print(a, "<", b)
else:
  print(a, "=", b)


#5.2 Check weather a number is odd or even
num=int(input("Enter a number:"))

if num%2==0:
  print(f"{num} is even")
else:
  print(f"{num} is odd")

#5.3 Check weather a number is prime of not

num=int(input("Enter a number:"))
f=0 
for i in range(2,num//2 +1):
 
  if num%i==0:
    print(f"{num} is not prime")
    f=1
    break

if f==0:
  print(f"{num} is prime")


#5.4 Conditional Checking - Compare strings
a=input("Enter a string: ")
b=input("Enter another string: ")

if a==b:
  print(f"{a} = {b}")

elif a>b:
  print(f"{a} > {b}")

else:
  print(f"{a} < {b}")


#Assignment 5 solutions:

#Assingment 5.1: WAP to find max amoung three numbers and input from user. [Try max() function]
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

maxVal=max(a,b,c)
print(f"Max value is: {maxVal}")

#Assingment 5.2: WAP to add all numbers divisible by 7 and 9 from 1 to n and n is given by the user.
n=int(input("Enter a number: "))
sum=0

for i in range(1,n+1):
  if i%7==0 and i%9==0:
    sum+=i

print(f"Sum of all numbers divisible by 7 and 9 from 1 to {n} is: {sum}")

#Assingment 5.3: WAP to add all prime numbers from 1 to n and n is given by the user.
n=input("Enter a number: ")
sum=0

for i in range(2,n+1):
  f=0
  for j in range(2,i//2 +1):
    if i%j==0:
      f=1
      break
  if f==0:
    sum+=i


print(f"Sum of all prime numbers from 1 to {n} is: {sum}")

#6 Functions

# 6.1 Add two numbers
def add(a,b):
  return a+b

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

add(a,b)

#6.2 Prime number

def isPrime(num):
  f=0
  for i in range(2,num//2 +1):
    if num%i==0:
      f=1
      break
  if f==0:
    return True
  else:
    return False
  
n=int(input("Enter a number: "))
print(isPrime(n))

#6.3 Add 1 to n

def addAll(n):
  sum=0
  for i in range(1,n+1):
    sum+=i
  return sum

n=int(input("Enter a number: "))


#7 Math library

import math as m

print("square root of 16 :" ,m.sqrt(16))
print("2 raised to power 3 :" ,m.pow(2,3))
print("log of 100 :" ,m.log(100))
print("log of 100 base 10", m.log10(100))
print("sin of 90 :" , m.sin(90))
print("cos of 90 :" , m.cos(90))
print("tan of 90 :" , m.tan(90))
print("Factorial of 5 :" , m.factorial(5))
print("Ceil of 4.5 :" , m.ceil(4.5))
print("Floor of 4.5 :" , m.floor(4.5))

#8 Strings

#8.1 Indexing in string


str="Hello World!"
print(str[0]) #H
print(str[6]) #W
print(str[-1]) #!
print(str[-6]) #W
print(str[-7]) #space
print(str[-12]) #H
print(str[0:5]) #Hello 0 is inclusive, 5 is exclusive
print(str[6:]) #World! 6 is inclusive, till end of string
print(str[:-5]) #Hello 0 is inclusive, -5 is exclusive
print(str[-6:]) #World! -6 is inclusive, till end of string

#8.2 String length, upper, lower
s=input("Enter a string: ")

print(f"Length of string is: {len(s)}")
print(f"Uppercase of string is: {s.upper()}")
print(f"Lowercase of string is: {s.lower()}")

#8.3 String formatting
name=input("Enter your name: ")
age=int(input("Enter your age: "))
price=float(input("Enter the price: "))

s="Name: %s, Age: %d, Price: %.2f" %(name.upper(), age, price)

#8.4 String in Triple Quotes
para_str = """This is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print(para_str)

#8.5 String strip
