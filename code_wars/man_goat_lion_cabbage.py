# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 15:04:17 2018

@author: RAVI SHANKAR SINGH
"""

# OOP VERSION OF MAN,GOAT,LION AND CABBAGE PROBLEM:

class animal(object):
    tag = 1
    def __init__(self,name,energy,riverside):
        self.name = name
        #self.category = category #herivore or carnivore
        self.energy = energy # +ve energy means carivore and vice-versa
        self.idnum = animal.tag
        self.riverside = riverside
        self.state = None
        animal.tag += 1
    
    def get_name(self):
        return self.name
    def get_energy(self):
        return self.energy
    def get_category(self):
        return self.category
    def get_idnum(self):
        return self.idnum
    def set_prey(self,animal2):
        if self.name == "man":
            return "man"
        else:
            if animal2.energy > self.energy:
                self.state = True
            else:
                self.state = False
    
    def get_state(self):
        return self.state

class boat(object):
    def __init__(self, permanent_member):
        self.member1 = permanent_member
        self.member2 = None
        self.riverside = 1
    
    def set_riverside(self, side):
        self.riverside = side
    def get_riverside(self):
        return self.riverside
# =============================================================================
#     def get_member1(self):
#         return self.member1
# =============================================================================
    def get_member2(self):
        return self.member2
    def set_member1(self, new_mem1):
        self.member1 = new_mem1
    def set_member2(self, new_mem2):
        self.member2 = new_mem2
    
class river(object):
    def __init__(self):
        self.side1_member = []
        self.side2_member = []
        
    def side1_add(self,ls):
        for i in ls:
            self.side1_member.append(i)
    def side2_add(self,ls):
        for i in ls:
            self.side2_member.append(i)
    def get_side1(self):
        return self.side1_member
    def get_side2(self):
        return self.side2_member

m = animal('man', 100,1)
g = animal('goat',20, 1)
l = animal('lion', 50, 1)
c = animal("cabbage",0, 1)












