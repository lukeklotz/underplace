import random

class Goblin:
    def __init__(self):
        self.health = 10
        self.attack = 1
        self.drop = {"coins" : 10, "stick" : 1, "goblin armor" : 1}

    #drop randomly selected from the "self.drops" list
    def random_drop_goblin(self):
        size = len(self.drop)

        drop_items = list(self.drop.keys())

        random_item = random.choice(drop_items)

        value = self.drop[random_item]

        print(f"Goblin dropped: {random_item} (Value: {value})")
        return value
    



        

    
