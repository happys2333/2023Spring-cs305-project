"""
This module helps you build a topology for Mininet
"""
import networkx as nx
import matplotlib.pyplot as plot

# using networkx to build a topology
class TopoGraph(nx.DiGraph):
    # topo of a network
    def __init__(self):
