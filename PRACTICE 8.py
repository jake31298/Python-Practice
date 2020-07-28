def compare(p1,p2):
    if(p1==p2):
        print("tie")
    elif(p1=="Rock" and p2=="Scissor"):
            print("Player one wins")
    elif(p1=="Paper" and p2=="Rock"):
        print("Player one wins")
    elif(p1=="Scissor" and p2=="Paper"):
            print("Player one wins")
    else:
            print("Player two wins")

Player_One=input("Please pick from the following:\nRock\nPaper\nScissor\n")
Player_Two=input("\nPlease pick from the following:\nRock\nPaper\nScissor\n")

compare(Player_One,Player_Two)

Play_Again=input("Do you want to play again y or n: ")
while(Play_Again=="y"):
    Player_One=input("Please pick from the following:\nRock\nPaper\nScissor\n")
    Player_Two=input("Please pick from the following:\nRock\nPaper\nScissor\n")
    compare(Player_One,Player_Two)