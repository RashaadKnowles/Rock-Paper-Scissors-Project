from game import Game
from player import Player
from computer import Computer
from human import Human

game_1 = Game()
game_1.intro_game()

player_1 = Player()
player_1.display_gestures()
player_1.choose_gesture()

AI = Computer()
AI.display_gestures()
AI.choose_gesture()