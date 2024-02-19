# Question2 -  Factorial Calculator

n = int(input("Enter a number:"))
fact=1
if n==0:
    print("The factorial of the number is 1")
elif n>0:
    while(n!=0):
        fact*=n
        n=n-1
    print("The factorial of the number is", fact)
else:
    print("Negative Numbers does not have a factorial")

