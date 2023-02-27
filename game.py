class Game():
    def __init__(self) -> None:
        pass 

    def intro_game(self):
        print("Welcome to RPSLS!!!")
        print("The Rules Are Simple")
        print("There will be 3 rounds to RSPLS!")
        print("Each player will choose a gesture.")
        print("Whoever's gesture is more powerful wins the round.")
        print("Best 2 out of 3 rounds WINS!!!")
        input("Would you like to play single or multiplayer?" )
        pass

    def run_game(self):
        option_1 = "Rock"
        option_2 = "Paper"
        option_3 = "Scissors"
        option_4 = "Spock"
        option_5 = "Lizard"
        while option_1 == "Rock" and option_2 == "Paper" and option_3 == "Scissors" and option_4 == "Spock" and option_5 == "Lizard":
            if option_1 < option_2:
                print("Paper wins")
            if option_1 > option_3:
                print("Rock wins")
            if option_1 < option_4:
                print("Spock wins")
            if option_1 > option_5:
                print("Rock wins")
            if option_2 < option_3:
                print("Scissors wins")
            if option_2 > option_4:
                print("Paper wins")
            if option_2 < option_5:
                print("Lizard wins")
            if option_3 < option_4:
                print("Spock wins")
            if option_3 > option_5:
                print("Scissors wins")
            if option_4 < option_5:
                print("Lizard wins")
        pass

    def display_winner(self):
        pass