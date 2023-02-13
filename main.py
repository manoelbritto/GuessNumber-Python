from art import logo
import random as rd

# Start game with Logo and status True
print (logo)
game_repeat = True

# Initial game number
initial_game_number = rd.randint(0,100)
print (initial_game_number)

#function with one parameter
def rate_guess (number):
    """ This function return if the guess is high or low
    accept just one argument
    """
    if number == initial_game_number:
        return "win"
    if abs(number-initial_game_number) > 5:
        return "High"
    else:
        return "Low"

#game play
while game_repeat:
    print ("This game is for you to guess a number between 0 to 100")
    game_level = input("To play, type which level you want Easy or Hard? ").lower()

    if game_level == 'easy':
        for _ in range(0,10):
            number_player = input("Type your number: ")
            result_game = rate_guess(int(number_player))
            if result_game == "win":
                break
            print(result_game)

        if result_game == "win":
            print("Congrats you win")
        else:
            print("Sorry you lose")

        game_ask = input("Would you like to continue yes or no? ").lower()
        if game_ask == 'yes':
            game_repeat = True

        else:
            game_repeat = False
