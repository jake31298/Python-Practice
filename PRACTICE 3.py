my_list = []
Input=""
while(True):
    Input=input("Please add a number\nType done when finished: ")
    if(Input=="done"):
        break
    my_list.append(int(Input))
    print("The current list is: " + str(my_list))
for element in my_list:
    if(element>5):
        print(element)
