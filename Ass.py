#Calculator: Create a simple calculator program that can perform basic arithmetic operations (addition, subtraction, multiplication, division) based on user input.
import pytest

x=int(input("Enter the value of X: "))
y=int(input("Enter the value of Y: "))

input_operation=input("Enter the operation to be perfomed use the first 3 letters as a word to perform operation like(add,sub,mul,div)anycases are accepted:")
input_operation.lower()
if input_operation=='add':
    result1=x+y
    print(f'The sum of two numbers is:{result1}')
elif input_operation=='sub':
    result2=x-y
    print(f'The difference of two numbers is:{result2}')
elif input_operation=='mul':
    result3=x*y
    print(f'The product of the two numbers is: {result3}')
elif input_operation=='div':
    result4=x/y
    print(f'The quotient of the two number is: {result4}')
else:
    print("Check the spelling of the operation which need to performed")
