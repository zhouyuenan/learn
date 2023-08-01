# ------------------------------------------------
# Program:
#       This Program is used to map the network topology
#       此项目用于绘制网络拓扑图
# History:
#       2023/07/30 周月南 First release
# ------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

node1 = '10.0.0.1'
node2 = '10.0.0.2'


def build_draw():
    graph = nx.DiGraph()
    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_edge('10.0.0.3', '10.0.0.4')
    nx.draw(graph, with_labels=True)
    plt.show()


def build_main():
    build_draw()


build_main()
# def fat_tree_topo(n=4):
#     """Standard fat tree topology
#     n: number of pods
#     total n^3/4 servers
#     """
#     topo = nx.Graph()
#     num_of_servers_per_edge_switch = n // 2
#     num_of_edge_switches = n // 2
#     num_of_aggregation_switches = num_of_edge_switches
#     num_of_core_switches = int((n / 2) * (n / 2))
#
#     # generate topo pod by pod
#     for i in range(n):
#         for j in range(num_of_edge_switches):
#             topo.add_node("Pod {} edge switch {}".format(i, j))
#             topo.add_node("Pod {} aggregation switch {}".format(i, j))
#             for k in range(num_of_servers_per_edge_switch):
#                 topo.add_node("Pod {} edge switch {} server {}".format(
#                     i, j, k))
#                 topo.add_edge(
#                     "Pod {} edge switch {}".format(i, j),
#                     "Pod {} edge switch {} server {}".format(i, j, k))
#
#     # add edge among edge and aggregation switch within pod
#     for i in range(n):
#         for j in range(num_of_aggregation_switches):
#             for k in range(num_of_edge_switches):
#                 topo.add_edge("Pod {} aggregation switch {}".format(i, j),
#                               "Pod {} edge switch {}".format(i, k))
#
#     # add edge among core and aggregation switch
#     num_of_core_switches_connected_to_same_aggregation_switch = num_of_core_switches // num_of_aggregation_switches
#     for i in range(num_of_core_switches):
#         topo.add_node("Core switch {}".format(i))
#         aggregation_switch_index_in_pod = i // num_of_core_switches_connected_to_same_aggregation_switch
#         for j in range(n):
#             topo.add_edge(
#                 "Core switch {}".format(i),
#                 "Pod {} aggregation switch {}".format(
#                     j, aggregation_switch_index_in_pod))
#
#     topo.name = 'fattree'
#
#     return topo
#
#
#
#
# topo = fat_tree_topo()
# nx.draw(topo, with_labels=True)
# plt.show()
