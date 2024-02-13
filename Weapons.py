from Player import Player

class Weapons:
    def __init__(self) -> None:
        self.weapon_list = [
            {
                "name" : "sword",
                "strength" : "20",
                "cost": "100"
            },
            {
                "name" : "axe",
                "strength" : "25",
                "cost" : "200"
            },
            {
                "name" : "staff",
                "strength" : "40",
                "cost" : "400"
            },
            {
                "name" : "knife",
                "strength" : "15",
                "cost" : "75"
            }
        ]
        
    def seeWeapons(self):
        for weapon in self.weapon_list:
            print(f"Name: {weapon['name']}, Strength: {weapon['strength']}")

    def weaponSelect(self, player):
        for weapon in self.weapon_list:
            print(f"Name: {weapon['name']}")
        
        viewing = True

        while viewing:
            item = input("Which item would you like to see? ").lower()
            found = False

            for weapon in self.weapon_list:
                if item == weapon['name']:
                    found = True
                
                    print(f"\nName: {weapon['name']}")
                    print(f"Strength: {weapon['strength']}")
                    print(f"Cost: {weapon['cost']}\n")

                    # ability to purchase the weapon
                    # and add to inventory
                    choice = input(f"Would you like to purchase this {weapon['name']}? (Y/N)")
                    if choice == 'Y':
                        player.aquireItem(weapon['name'])


                    done = input("Continue looking? (Y/N)\n").upper()
                    if done == 'N':
                        viewing = False
                        break

            if not found:
                print(f"{item} is not in the list\n")

