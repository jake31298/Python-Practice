num = input("Please give a number to divide\n")
while(not num.isnumeric()):
    num = input("Please try again\n")

num=int(num)

divisor = range(1,num+1)

list_of_divisors=[]

for a in divisor:
    if((num%a)==0):
        #print(str(num)+" is able to be divided by " + str(a) +" evenly")
        list_of_divisors.append(a)
    #print(num/a)

print(list_of_divisors)