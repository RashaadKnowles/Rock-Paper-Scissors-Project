from player import Player
class Human(Player):
    def __init__(self):
          self.gesture_list
          super().__init__()
            
    def display_gestures(self):
        for character in self.gesture_list:
            print(character)
        

    def choose_gesture(self):
        user_input = input("Which do you choose Rock,Paper,Scissors,Lizard,Spock?")
       
        if user_input in self.gesture_list:
            self.selected_gesture = user_input
        
        
    