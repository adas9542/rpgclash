from classes.game import Person, bcolors
import random

magic = [{"name": "Fire", "cost": 15, "dmg": 70},
{"name": "Ice", "cost": 13, "dmg": 65},
{"name": "Lightning", "cost": 16, "dmg": 67},
{"name": "Poison", "cost": 12, "dmg": 62},
]

player = Person(400, 70, 71, 32, magic)

enemy = Person(1200, 65, 45, 25, magic)

i = 1
while 1:
    print("=======Your Turn=========")
    player.choose_magic()
    choice = input("Which magic do you choose? : ")
    upd_option = int(choice) - 1
    print("You chose " + player.get_spell_name( upd_option ))
    damage_inflicted = player.gen_spelldmg(upd_option)
    enemy.take_dmg(damage_inflicted)
    print("Enemy has lost ", damage_inflicted, " hp1. Enemy hp: ", enemy.hp)

    print("==============Enemy's Turn================")
    enemy.choose_magic()
    enemy_choice = enemy.gen_spelldmg(random.randrange(0,4))
    enemy_damage = int(enemy_choice)
    player.take_dmg(enemy_damage)
    print("You has lost ", enemy_damage, " hp1. Your hp: ", player.hp)

    i = 0


print(bcolors.FAIL + bcolors.BOLD + "Enemy Attacks!" + bcolors.ENDC)

