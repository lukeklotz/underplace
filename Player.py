class Player:
    def __init__(self) -> None:
        self.health = 100
        self.energy = 100
        self.inventory = []
        self.skills = []
        self.coins = 0
        pass
    
    def aquireItem(self, item) -> None:
        self.inventory.append(item)

    def seeInventory(self) -> None:

        size = (len(self.inventory))
        
        if size < 0:
            print("Inventory empty!")
            return
        
        for i in range(size):
            print(self.inventory[i])


    def seeStats(self) -> None:
        print("\n+---------------------+")
        print(f"Health: {self.health}")
        print(f"Energy: {self.energy}")
        print(f"Coins: {self.coins}")
        print("+---------------------+\n")

    