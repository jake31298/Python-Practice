
my_list = []
Input=""
while(True):
    Input=input("Please add a number\nType done when finished: ")
    if(Input=="done"):
        break
    my_list.append(int(Input))
    print("The current list is: " + str(my_list))
for element in my_list:
    if(element<5):
        print(element)


#a=[1,55,6,7,8,9,7,7,8,6,8,66,8,6,8,6,8,6]
#print([aa for aa in a if aa > 5])