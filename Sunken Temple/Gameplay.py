#At this early point, gameplay just has a list of characters that get created at
# runtime, and calls the char_stats frame creator/populator for each.

import random
from Character_Class import Character
import Gui as g
import options

class New_Game():
    def __init__(self):
        self.players = []
        self.colorbank = ["coral", "darkolivegreen", "dodgerblue", "darkviolet",
                          "orangered", "darkslategray", "dimgray", "salmon", "sienna",
                          "goldenrod", "yellow", "black"]
        self.gui = g.Gui(self)
        self.opt = options.Options(self)

    def assign_color(self):
        color = random.choice(self.colorbank)
        self.colorbank.remove(color)
        return color

    def add_player(self, name, **kwargs):
        p_color = self.assign_color()
        player = Character(name, color = p_color, **kwargs)
        self.players.append(player)
        self.gui.add_char_stats(player)

    def text_parse(self, text_string):
        text_string = text_string.lower()
        text_string = text_string.replace("'", " ").strip()
        #TODO: look into regex to split properly around punctuation, including
        #      apostrophes, periods, etc.
        words = text_string.split()
        self.opt.interpret(*words)

if __name__ == "__main__":
    game = New_Game()
    game.add_player("Dave", level=8, strength=2, intellect=18)
    game.add_player("Victoria", level=6, strength=17, spirit=9)
    game.add_player("Frank", level=6, strength=3, intellect=20, spirit=12)