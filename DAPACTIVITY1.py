#1. Calculate the multiplication and sum of two numbers
a=int(input("enter a value for a:"))
b=int(input("enter a value for b:"))
S=a+b
M=a*b
print("sum of a and b:",S)
print("product of a and b:",M)


#Program to perform addition, subtraction, multiplication and division on two input numbers in Python
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)


#2.Declare two variables and print that which variable is largest using ternary operators

a=int(input("enter a value for a:"))
b=int(input("enter a value for b:"))
largest=a if a>b else b
print(
"the largest variable is:",largest)

#3.Declare two variables and print that which variable is largest using ternary operators

a=int(input("enter a value for a:"))
b=int(input("enter a value for b:"))
largest=a if a>b else b
print(
"the largest variable is:",largest)

#4. Python program to find the area of a triangle whose sides are given
base=float(input("Enter the base:")) 
height=float(input("Enter the height:")) 
area =1/2*(base*height)
print("The area of the triangle is:", area)


#4. Python program to find the area of a triangle whose three sides are given
a=float(input("Enter first side:"))
b=float(input("Enter second side:"))
c=float(input("Enter third side:"))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the triangle is:",area)

#5.Write a Python program to check whether a number is even or odd
input_number=int(input("type a number:"))
if input_number % 2==0:
    print(input_number,"is a even number")
else:
    print(input_number,"is a odd number")

#6.Find the square and cube of a given number.
number=int(input("enter a number:"))
square=number*number
cube=number*number*number
print("the square of the number is:",square)
print("the cube of the number is:",cube)





