# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(0)
list_1=[]
list_2=[]
list_3=[]
# generate some integers
for a in range(25):
	value = randint(0, 20)
	list_1.append(value)

for b in range(20):
    value = randint(0, 20)
    list_2.append(value)


for c in list_1:
    if(c in list_2):
        list_3.append(c)
        list_3.sort()

print(list_1)
print(list_2)
print(list_3)
