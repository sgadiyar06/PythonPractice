# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 11:32:22 2020

@author: Sudarshan
"""


import networkx as nx
import matplotlib.pyplot as plt

G=nx.complete_graph(20)

nx.draw(G)
plt.show()