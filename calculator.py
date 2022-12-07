a=int(input("Enter First Number: "))
b=input("Enrter operator: +,-,*,//,%: ")
c=int(input("Enter Second Number: "))

if b=="+":
    print("Sum is:",a+c)
elif b=="-":
    print("Subtraction is:",a-c)
elif b=="*":
    print("Multiplication is:",a*c)
if b=="//":
    print("Divide is:",a//c)
if b=="%":
    print("Remainder is:",a%c)
    