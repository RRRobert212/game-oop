#constants.py

race_list = ["Human", "Elf", "Dwarf"]
race_health = [[75,125], [50, 100], [100,150]]
race_attack = [[20,35], [25,50], [15,30]]

enemy_list = ["Goblin", "Troll"]
enemy_health = [[30,40], [20,30]]
enemy_attack = [[10,20],[20,30]]

#weapon ids are just their index in this list, same for other lists
weapon_names = ["Fists", "Old Stick", "Decent Sword"]
weapon_damage_factor = [[0.175,0.275], [0.2, 0.4], [0.5,0.7]]

armor_names = ["leather shirt"]
armor_block_factor = [[0.2,0.3]]

consumable_names = []
consumbale_effect_factor = [[]]

#lists to keep track of enemies and items that are currently on the map. Used for collision detection
spawned_enemies =[]
spawned_items = []
spawned_character = []




