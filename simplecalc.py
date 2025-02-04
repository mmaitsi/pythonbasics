# prompt user to enter two numbers
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

# prompt user to select operator
operator=input("Enter an operator(+,-,*,/): ")
# perform calculation based on operator
if operator=="+":
    result=num1+num2
elif operator=="-":
    result=num1-num2
elif operator=="*":
    result=num1*num2
elif operator=="/":
    if num2 != 0:
        result=num1/num2
    else:
        result="Error, division by zero"
else:
    result="Invalid operator"
print(f"The result is: {result}")

