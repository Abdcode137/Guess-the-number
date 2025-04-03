import random 

attempts_list = []

def show_score():
    if len(attempts_list) <= 0:
        print("There is ccurrently no high score, it's yours for the talking!")
    else:
        print(f"The current high scroe is {min(attempts_list)} attempts")

def start_game():
    random_number = random.randint(1, 10)
    player_name = input("Hey there! Welcome to the game of guesses! \n Enter your name:")
    wanna_play = input(f"Hi, {player_name}, would you like to play the guessig game ? (Enater Yes/No)")
    
    while wanna_play.lower() == "yes":
        try:
            guess= int(input("Pick a number between 1 to 10"))
            if guess < 1 or guess > 10:
                raise ValueError("Please guess a number within the given range ")
            if guess == random_number:
                print("Congrats! You have guessed it right!")
                attempts = 1
                attempts_list.append(attempts)
                print(f"It took you {attempts} attempts")
                play_again = input ("Would you like to play again ? (Enter Yes/No)")
                attempts = 0
                show_score()
                random_number = random.randint(1, 10)
                if play_again.lower == "no":
                    print("That's cool have a nice day!")
                    break
                elif guess < random_number:
                    print("It's lower" )
                    attempts += 1
                elif guess >  random_number:
                    print("It's higher" )
                    attempts += 1
        except ValueError as err:
            print(f"Oh! that's not a valid value. Try again ......  {err}")
        except Exception as err:
            print(f"An unexpected error occurred : {err}")
    else:
        print("That's cool! Have a nice day!")
if __name__ == "__main__":
    start_game()