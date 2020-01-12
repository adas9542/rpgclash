import random

class bcolors:
    Header = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk -10
        self.atkh = atk + 10
        self.df = df
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def gen_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def gen_spelldmg(self, i):
        mgl = self.magic[i]["dmg"]-5
        mgh = self.magic[i]["dmg"]+5
        return random.randrange(mgl,mgh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def get_maxhp(self):
        return self.maxhp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self,i):
        return self.magic[i]["name"]

    def spell_mp_cost(self,i):
        return self.magic[i]["cost"]

    def choose_action(self):
        print("Actions")
        i = 1
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_magic(self):
        print("Magic")
        i = 1
        for spell in self.magic:
            print(str(i) + ":", spell["name"], "(cost:", str(spell["mp"]) + ")" )
            i += 1