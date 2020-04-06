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

infection_rate = 0.2
recovery_rate = 0.01

class Bacteria(Agent):
    def __init__(self, unique_id,model,state=0,age=0,volume=0.1,tax='bac',gene_arg=None,mge=None):
        super().__init__(unique_id, model)
        self.unique_id = unique_id
        self.model = model
        self.state = state # 0 susceptible; 1 infected; 2 recovered
        self.age=age
        self.volume = volume
        self.tax = tax
        self.gene_arg = gene_arg
        self.mge = mge

    def step(self):
        self.random_move()
        self.divide()
        self.grow()
        self.interact()



    def random_move(self):
        ''' Bacteria can randomly move to nearby grids'''
        neighbor_pos = self.model.grid.get_neighborhood(self.pos, moore=True,include_center=False)
        new_pos = random.choice(neighbor_pos)
        self.model.grid.move_agent(self,new_pos)

    def grow(self):
        self.age += 1
        self.volume = 0.1 + self.age*0.005

    def divide(self):
        if self.volume == 0.2: # divide when the bacteria reaches 20 time steps
            self.age = 0
            new_born = Bacteria(self.model.num_agents+1,self.model,
            self.state,0,0.1,self.tax,self.gene_arg,self.mge) # inherit the genes from parent cell
            self.model.grid.place_agent(new_born,self.pos)
            self.model.schedule.add(new_born)
            self.model.num_agents += 1

    def interact(self):
        ''' interact with bacteria located in the same grid'''
        # search the agents located in the same grids

        if self.state == 1:
            x, y = self.pos
            this_cell = self.model.grid.get_cell_list_contents([self.pos])
            susceptible_bacteria = [obj for obj in this_cell if obj.state==0]
            # randomly infected a susceptible_bacteria
            if len(susceptible_bacteria)>0:
                for each in susceptible_bacteria:
                    # randomly sample a number p, if p<infection rate, infection happens
                    p = random.uniform(0,1)
                    if p< infection_rate:
                        each.state = 1
                        each.gene_arg = self.gene_arg

            # after infection, there is a chance to recovered
            p = random.uniform(0,1)
            if p<recovery_rate:
                self.state = 2
