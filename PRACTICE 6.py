Test=input("Please type a string: ")
Test=Test.lower()
length=len(Test)
for letter in Test:
    if(not letter==Test[length-1]):
        print("It's not a palindrome aw")
        break
    length=length-1
    if(l==0):
        print("It's a palindrome yay")