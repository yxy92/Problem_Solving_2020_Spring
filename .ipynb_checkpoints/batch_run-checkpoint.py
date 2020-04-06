# Batch Run

from mesa.visualization.modules import CanvasGrid, ChartModule
from MesaBacteria.agent import Bacteria
from MesaBacteria.model import Bacteria_Colony
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

batch_size = 100
step_size = 40
type_num = 3
infected_rate = [0.01,0.03,0.05]

result_table = np.zeros((len(infected_rate),batch_size,type_num))
for i in range(len(infected_rate)):
    for j in range(batch_size):
        model = Bacteria_Colony(100,10,10,infected_rate[i])
        model.run_model(step_size)

        susceptible_num=model.count_head(0)
        infected_num=model.count_head(1)
        recovered_num=model.count_head(2)
        total_num = susceptible_num+infected_num+recovered_num

        result_table[i,j,0] = susceptible_num/total_num
        result_table[i,j,1] = infected_num/total_num
        result_table[i,j,2] = recovered_num/total_num



# plot
fig=plt.figure()
ax=Axes3D(fig)
scatter1=ax.scatter(result_table[0,:,0],result_table[0,:,1],result_table[0,:,2],c='blue',label='ARG1')
ax.scatter(result_table[1,:,0],result_table[1,:,1],result_table[1,:,2],c='red',label='ARG2')
ax.scatter(result_table[2,:,0],result_table[2,:,1],result_table[2,:,2],c='green',label='ARG3')

ax.legend()
ax.set_xlabel('Susceptible')
ax.set_ylabel('Infected')
ax.set_zlabel('Recovered')
plt.show()
