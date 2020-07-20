Number=input("Please enter a whole number\n")
while(not Number.isnumeric()):
    Number=input("Try again")
Number=int(Number)
if((Number%2)==0):
    print("It's even yay!")
else:
    print("Not an even number :(\n")

if(int(Number%4)==0):
    print("It's divisible by 4 neat")