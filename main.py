import Utility
from Player import Player
from Weapons import Weapons
from World import World
quit = False

#initialize player
#see Player.py def__init__
player = Player()

#not sure if shop should be its own thing with
#the weapons class as part of it..
#but for not we'll just do this

shop = Weapons() 
world_map = World()

while quit != True:
    choice = Utility.menuSelect()
    if choice == "1":
        shop.weaponSelect(player)
    if choice == "2":
        player.seeStats()
    if choice == '3':
        player.seeInventory()
    if choice == '4':
        world_map.where_am_i()
    if choice == '5':
        world_map.travel()
    if choice =='6':
        world_map.check_monsters()  
    if choice == '7':
        print("coming soon!")
    if choice == '8':
        world_map.check_resources()
        
    if choice == "99":
        quit = True
    

print("goodbye!")
