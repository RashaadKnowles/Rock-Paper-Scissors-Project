class Player():

    def __init__(self) -> None:
        self.gesture_list =["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.selected_gesture = None

    def display_gestures(self):
        for character in self.gesture_list:
            print(character)

# TODO: Check if user_input is an option in self.gesture_list
        # If it is, set self.selected_gesture to their choice
    def choose_gesture(self):
        user_input = input("Which do you choose Rock,Paper,Scissors,Lizard,Spock?")
       
        if user_input in self.gesture_list:
            self.selected_gesture = user_input 


            

        
