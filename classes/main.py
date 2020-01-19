from classes.game import Person, bcolors
from classes.magic import Spell

import random
import math

fire = Spell("Fire", 25, 370, "Black")
ice = Spell("Ice", 13, 265, "Black")
lightning = Spell("Lightning", 16, 267, "Black")
poison = Spell("Poison", 12, 250, "Black")
cure = Spell("Cure", 15, 70, "White")

magic = [{"name": fire.name, "cost": fire.cost, "dmg": fire.dmg, "type": fire.type},
         {"name": ice.name, "cost": ice.cost, "dmg": ice.dmg, "type": ice.type},
         {"name": lightning.name, "cost": lightning.cost, "dmg": lightning.dmg, "type": lightning.type},
         {"name": poison.name, "cost": poison.cost, "dmg": poison.dmg, "type": poison.type},
         {"name": cure.name, "cost": cure.cost, "dmg": cure.dmg, "type": cure.type}]

player = Person(400, 70, 71, 32, magic)

enemy = Person(1200, 65, 45, 25, magic)

i = 1


def mp_valid(player_mp, mp_cost):
    return int(player_mp) - mp_cost


def stats_calc(x, spell_cost, damage, type):
    if (x == 2 and type == "Black"):
        player.mp -= spell_cost
        enemy.take_dmg(damage)
    elif (x == 1 and type == "Black"):
        enemy.take_dmg(damage)
    elif (x == 2 and type == "Black" and player.maxhp != player.mp):
        player.hp += damage


def act_statement():
    print("==============Your Turn==================")
    player.choose_action()
    act = input(bcolors.OKBLUE + "Which action do you choose? : " + bcolors.ENDC)
    return act


def magic_option():
    player.choose_magic()
    choice = input(bcolors.OKBLUE + "Which magic do you choose? : " + bcolors.ENDC)
    upd_magic = int(choice) - 1
    return upd_magic


def domagic(option, valid):
    if int(valid) > 0:  # use magic spell
        damage_inflicted = player.gen_spelldmg(option)
        spell_cost = player.spell_mp_cost(option)
        spell_name = player.get_spell_name(option)
        type = player.get_type(option)
        stats_calc(int(action), spell_cost, damage_inflicted, type)
        print("You chose " + spell_name)
        return damage_inflicted
    elif int(valid) <= 0:
        print(bcolors.BOLD + "You don't have enough magic points" + bcolors.ENDC)


def doattack():
    spell_cost = 0
    damage_inflicted = player.gen_damage()
    type = "None"
    stats_calc(int(action), spell_cost, damage_inflicted, type)
    print(bcolors.BOLD + bcolors.OKGREEN + "You have attacked" + bcolors.ENDC)
    return damage_inflicted


while 1:
    action = int(act_statement())
    if action == 2: #cure does not work
                    #attack by itself does not work
                    #enemy is unable to reach 0 hp
        option = magic_option()
        valid = mp_valid(player.mp, player.spell_mp_cost(option))
        damage_inflicted = domagic(option, valid)

    if action == 1 or valid <= 0:
        damage_inflicted = doattack()

    print("Enemy has lost", damage_inflicted, "hp.")
    print("===============Stats=====================")
    print("Enemy hp:", enemy.hp, "\nYour hp:", player.hp, "\nYour mp:", player.mp)

    print("=============Enemy's Turn================")
    enemy_dmg = enemy.gen_damage()
    player.take_dmg(enemy_dmg)
    print(bcolors.FAIL + bcolors.BOLD + "Enemy attacks:", "\nYou lost ", enemy_dmg, " hp. You have", player.get_hp(),
          "hp left.", bcolors.ENDC)
    if player.hp == 0:
        print(bcolors.FAIL + bcolors.BOLD + "Battle is Over. You have lost!" + bcolors.ENDC)
        break
    if enemy.hp == 0:
        print(bcolors.OKGREEN + "\nYou have defeated the enemy!" + bcolors.ENDC)
        break
    i = 0
