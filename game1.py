import random

player_win=0
computer_win=0

def player_choice():
    player_pick=input("choose among 'Rock','Paper','Scissors' :")
    if player_pick in ["Rock","rock","r","R"]:
        player_pick="r"
    elif player_pick in ["Paper","paper","p","P"]:
        player_pick="p"
    elif player_pick in ["Scissors","scissors","s","S"]:
        player_pick="s"
    else:
        print("I don't understand , try again")
        player_choice()

    return player_pick

def computer_choice():
    comp_pick=random.randint(1,3)
    if comp_pick==1:
        comp_pick="r"
    elif comp_pick==2:
        comp_pick="p"
    elif comp_pick==3:
        comp_pick="s"
    

    return comp_pick

while True:
    player_turn=player_choice()
    comp_turn=computer_choice()

    print("")
    if player_turn=="r":
        if comp_turn=="r":
            print("you choose Rock, computer also choose Rock, So it is a draw")
        elif comp_turn=="p":
            print("you choose Rock, computer choose Paper, so computer wins")
            computer_win+=1
        elif comp_turn=="s":
            print("you choose Rock, computer choose Scissors, so you win")
            player_win+=1

    elif player_turn=="p":
        if comp_turn=="r":
            print("you choose Paper, computer choose Rock, so you win")
            player_win+=1

        elif comp_turn=="p":
            print("you choose paper, computer also choose paper, so it is a draw")

        elif comp_turn=="s":
            print("you choose paper, computer choose Scissors, so computer wins")
            computer_win+=1

    elif player_turn=="s":
        if comp_turn=="r":
            print("you choose scissors, computer choose Rock, so computer wins")
            computer_win+=1
        elif comp_turn=="p":
            print("you choose scissors, computer choose Paper, so you win")
            player_win+=1
        elif comp_turn=="s":
            print("you choose scissors, computer choose scissors, so it is a draw")


    print("So final result:---")

    print("computer: "+str(computer_win)+"        "+"Player: "+str(player_win))

    print("")

    val=input("do you want to play more:(y/n)")

    if val=="y":
        pass
    elif val=="n":
        print("So final result:---")
        print("computer: "+str(computer_win)+"        "+"Player: "+str(player_win))
        break
    else:
        break
    








