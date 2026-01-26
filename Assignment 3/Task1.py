def factorial(num):
    for i in range (num,1,-1):
        num = num * (i-1)
    return num

number = int(input("Enter a number : "))   
print(f"factorial of {number} is: {factorial(number)}")
