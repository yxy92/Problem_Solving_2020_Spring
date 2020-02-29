# Mesa_Bacteria server

from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from MesaBacteria.agent import Bacteria
from MesaBacteria.model import Bacteria_Colony

def Bacteria_portrayal(agent):
    portrayal = {}
    if agent.state == 0:
        portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "red",
                 "r": agent.volume}

    elif agent.state == 1:
        portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "yellow",
                 "r": agent.volume}

    else:
        portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "blue",
                 "r": agent.volume}
    return portrayal


canvas_element = CanvasGrid(Bacteria_portrayal, 20, 20, 400, 400)
chart_element = ChartModule([{"Label": "Susceptible", "Color": "#AA0000"},
                             {"Label": "Infected", "Color": "#FFFF00"},
                             {"Label": "Recovered", "Color": "#0000FF"},])

server = ModularServer(Bacteria_Colony, [canvas_element, chart_element],
"Bacteria", {"N":400, "width":20, "height":20})


server.port = 8521
server.launch()
