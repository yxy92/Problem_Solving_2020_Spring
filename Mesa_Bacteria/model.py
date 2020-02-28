# Mesa_Bacteria model
from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import random
from .agent import Bacteria


class Bacteria_Colony(Model):
    def __init__(self,N,width,height):

        self.num_agents = N
        self.width =width
        self.height = height
        self.grid = MultiGrid(width,height,True)

        self.schedule = RandomActivation(self)

        # DataCollector
        self.datacollector = DataCollector(
                {"Susceptible":lambda m: m.count_head(0),
                 "Infected": lambda m: m.count_head(1),
                 "Recovered": lambda m: m.count_head(2)})
                 # m corresponds to the model, which is the argument of the function

        # create and assign agents
        coords_list = [(x,y) for x in range(width) for y in range(height)]

        for i in range(self.num_agents):
            # randomly assign the agent to a cell
            coords = random.choice(coords_list)
            #print(coords)
            state = random.choice([0,1,2])
            a = Bacteria(i,self,state)
            self.grid.place_agent(a, coords)
            self.schedule.add(a)

        self.running=True
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)

    def run_model(self,step_count=200):
        for i in range(step_count):
            #print("The model is currently running step %d" % (i))
            self.step()

    def count_head(self,type):
        # type 0: Susceptible, 1: Infected, 2: Recovered
        count = 0;
        tmp = self.schedule._agents
        for each in tmp.values():
            if each.state == type:
                count+=1
        return count

if __name__ == "__main__":
    model = Bacteria_Colony(100,10,10)
    model.run_model()

    susceptible_num=model.count_head(0)
    print("The susceptible agent number is %d" %(susceptible_num))
    infected_num=model.count_head(1)
    print("The infected agent number is %d" %(infected_num))
    recovered_num=model.count_head(2)
    print("The recovered agent number is %d" %(recovered_num))
