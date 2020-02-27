# Mesa_Bacteria agent
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:52:06 2020

@author: xiangyuyao
"""
#############################


from mesa import Agent
from mesa

class Bacteria(Agent):
    def __init__(self, unique_id,model,state=0):
        '''
        Args:
            unique_id: unique identifier
            pos: (x,y) Agent initial location
            status: 'On' or 'Off' to indicate the status of the light

        '''
        super().__init__(unique_id, model)
        self.unique_id = unique_id
        self.model = model
        self.state = state

    def step(self):
