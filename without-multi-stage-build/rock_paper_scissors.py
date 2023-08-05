
def players_choice_input():
    while True:
        players_choice= input("Please enter your choice(rock/paper/scissors: ").lower()
        if players_choice in ["rock", "paper" ,"scissors"]:
            return players_choice
        else:
            print("Invalid input . Please choose 'rock','paper' or 'scissors'.")

def game_winner(player1_input, player2_input):
    if player1_input==player2_input:
        print("IT'S A TIE")
    elif(player1_input == "rock" and player2_input=="scissors") or \
        (player1_input == "paper" and player2_input=="rock") or \
        (player1_input == "scissors" and player2_input=="paper"):

        return "Player 1 wins"
    else:
        return " Player 2 wins "

    
def game_start():
    print("Let's do rock, paper , scissors!")
    player1_answer = players_choice_input()
    player2_answer= players_choice_input()

    print(f"player 1 choice : {player1_answer}")
    print(f"player 2 choice : {player2_answer}")

    result = game_winner(player1_answer,player2_answer)

    print(result)

if __name__ == '__main__':
    game_start()