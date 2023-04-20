"""
This module helps you build a topology for Mininet
"""
import warnings

import matplotlib
import networkx as nx
import matplotlib.pyplot as plot

# let you can run in a remote server
matplotlib.use('Agg')


# using networkx to build a topology
class TopoGraph(nx.DiGraph):
    # topo of a network
    def __init__(self, name):
        super(TopoGraph, self).__init__()
        warnings.filterwarnings("ignore", category=UserWarning)
        self.plot_options = {
            "font_size": 20,
            "node_size": 1500,
            "node_color": "white",  # 节点背景颜色
            "linewidths": 3,
            "width": 3,
            "with_labels": True
        }
        self.pos = nx.spring_layout(self)
        plot.figure(1, figsize=(25, 25))
        plot.ion()

    def shortest_path(self, node1, node2) -> list:
        # TODO: find the shortest path between node1 and node2
        # Return a list of the shortest path
        pass

    def longest_path(self, node1, node2) -> list:
        # TODO: find the longest path between node1 and node2
        # Return a list of the longest path
        pass

    def draw_path(self, path: list):
        # TODO: use matplotlib to draw the path and save as a picture file
        pass
