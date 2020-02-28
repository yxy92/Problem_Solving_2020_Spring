# Mesa_Bacteria agent
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:52:06 2020

@author: xiangyuyao
"""
#############################


from mesa import Agent
import random
from mesa import space

class Bacteria(Agent):
    def __init__(self, unique_id,model,state=0,tax='bac',gene_arg='mce',mge="afg"):
        super().__init__(unique_id, model)
        self.unique_id = unique_id
        self.model = model
        self.state = state
        self.tax = tax
        self.gene_arg = gene_arg
        self.mge = mge

    def step(self):
        self.random_move()



    def random_move(self):
        ''' Bacteria can randomly move to nearby grids'''
        neighbor_pos = self.model.grid.get_neighborhood(self.pos, moore=True,include_center=False)
        new_pos = random.choice(neighbor_pos)
        self.model.grid.move_agent(self,new_pos)
