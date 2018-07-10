import random
import string

class Game():
    def __init__(self):
        self.grid = []
        while len(self.grid) < 9:
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, data):
        if data == "":
            return False
        grid2 = self.grid.copy()
        for i in data:
            try:
                grid2.remove(i)
            except:
                return False
        return True
