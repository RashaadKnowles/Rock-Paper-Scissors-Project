import random
from player import Player
class Computer(Player):
    def __init__(self):
        super().__init__()

    def display_gestures(self):
        for character in self.gesture_list:
            print(character)
        
       
    def choose_gesture(self):
        self_gesture_list = random.choice(self.gesture_list)
        print(self_gesture_list)
     
