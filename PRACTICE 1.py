from datetime import datetime

year = datetime.now().year
#print(year)

age =input("How old are you?\n")
while(not age.isnumeric()):
    age=input("You didn't enter a number.\nTry again.")
age =int(age)
year=(year - age) + 100
years=100-age
if(years==0):
    print("Wow you are 100")
elif(years<0):
    print("Wow you are older then 100")
else:
    print("You'll be 100 in " + str(years) +" years")
    print("The year that you'll be 100 is " + str(year))