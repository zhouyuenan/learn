# ------------------------------------------------
# Program:
#       This Program is used to map the network topology
#       此项目用于绘制网络拓扑图
# History:
#       2023/07/30 周月南 First release
# ------------------------------------------------
# 1.根据IP范围确定顶点大小；
# 2.从Excel文件中读取数据；
# 3.画出3D网络拓扑图；
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

node1 = '10.0.0.1'
node2 = '10.0.0.2'


def build_obtain_data(file_name):
    """此函数用于读取Excel文件中的数据。"""
    print("test")


def build_draw():
    """此函数用于绘制网络拓扑图。"""
    graph = nx.DiGraph()
    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_edge('10.0.0.3', '10.0.0.4')
    ip_range = 24
    if ip_range == 16:
        node_size_range = 10000
    elif ip_range == 24:
        node_size_range = 1000
    elif ip_range == 32:
        node_size_range = 100
    nx.draw(graph, with_labels=True, node_size=node_size_range)
    x = np.linspace(0.05, 10, 1000)
    y = np.sin(x)
    plt.plot(x, y, label="topology network graph")
    plt.legend(loc="lower left")
    plt.xlim(-10, 10)
    plt.ylim(-1, 1)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("topology Network Security Groups")
    plt.show()


def build_main():
    """此函数用于主函数入口。"""
    build_obtain_data(file_name="test")
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
