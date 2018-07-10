import random
import string
import requests

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
        url = "https://wagon-dictionary.herokuapp.com/" + str(data)
        response = requests.get(url)
        if not response.json()["found"]:
            return False
        return True
