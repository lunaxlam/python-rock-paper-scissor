from random import choice

def player_turn():
    """Return the player's selection"""

    while True:

        player_selection = input("Select rock, paper, or scissor: ").lower()

        if player_selection == "rock" or player_selection == "paper" or player_selection == "scissor":

            return player_selection
        else:
            print("Not an option. Try again!")
        

def computer_turn():
    """Return the computer's selection"""

    choices = ["rock", "paper", "scissor"]
    
    computer_selection = choice(choices)

    print(f"The computer selected: {computer_selection}")

    return computer_selection


def play_round():
    """Play a round of rock, paper, scissor"""

    player_selection = player_turn()
    computer_selection = computer_turn()

    if player_selection == computer_selection:
        print(f"Player and Computer both chose {player_selection}. This round is a tie!")
        return None
    elif player_selection == "rock" and computer_selection != "paper":
        print(f"{player_selection} beats {computer_selection}! 1 point to Player.")
        return "player"
    elif computer_selection == "rock" and player_selection != "paper":
        print(f"{computer_selection} beats {player_selection}! 1 point to Computer.")
        return "computer"
    elif player_selection == "paper" and computer_selection != "scissor":
        print(f"{player_selection} beats {computer_selection}! 1 point to Player.")
        return "player"
    elif computer_selection == "paper" and player_selection != "scissor":
        print(f"{computer_selection} beats {player_selection}! 1 point to Computer.")
        return "computer"
    elif player_selection == "scissor" and computer_selection != "rock":
        print(f"{player_selection} beats {computer_selection}! 1 point to Player.")
        return "player"
    elif computer_selection == "scissor" and player_selection != "rock":
        print(f"{computer_selection} beats {player_selection}! 1 point to Computer.")
        return "computer"


def main():
    """Play multiple rounds of rock, paper, scissor, and keep track of the score. 
    
    Print the total score and winner."""

    rounds = 5
    player_score = 0
    computer_score = 0

    while rounds > 0:
        winner = play_round()
        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1
        rounds -= 1
    
    print()
    print("*** Final Scores *** ")
    print(f"Player: {player_score}. Computer: {computer_score}.")

    if player_score > computer_score:
        print("Player 1 wins!")
    elif computer_score > player_score:
        print("Computer wins!")
    else:
        print("No winners. The game is tied.")
        
    
if __name__ == "__main__":
    main()

