from graph_utils import Graph, Node
from queue import PriorityQueue
from collections import defaultdict
import turtle
import os

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path = [current] + total_path
    return total_path


def a_star(start, goal, h):
    """
        a-star finds a short path from start to goal 

        h is a heuristic function h(n, goal) that estimates the distance/cost
        to reach 'goal' from node 'n'
    """
    #PriorityQueue accepts tuple
    #(distance, neighboring node)
    open_set = PriorityQueue()

    # Fpr came_from[n], it is the node that came from the shortest path from start to n 
    # currently known
    came_from = {}

    #initializing the default distance
    #g_score: shortest distance between any two points 
    #(one being the current and the other neighbouring node)
    g_score = defaultdict(lambda: float('inf'))

    #There's no distance between start and start.
    #Initializing distance at the first node
    g_score[start] = 0

    #the f_score is the distance from start to goal
    f_score = defaultdict(lambda: float('inf'))
    distance_initial = h(start,goal)
    f_score[start] = distance_initial

    #start exploring
    #putting a tuple
    #open_set is prioritizing DISTANCES of node start's neighbors
    open_set.put((distance_initial, start))

    while not open_set.empty():
        #tuple is distance and current node
        #_, is distance. It is a "throaway variable"
        _, current = open_set.get()

        if current == goal:
            path = reconstruct_path(came_from, current) 
            print(type(path))
            return path

        for neighbor, weight in current.get_weighted_neighbors():
            #tentative_g_score: distance from start to the neighbor
            #through current
            tentative_g_score = g_score[current] + weight

            #Found the shortest node
            if tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + h(neighbor, goal)
                came_from[neighbor] = current
                if neighbor not in open_set.queue:
                    open_set.put((f_score[neighbor], neighbor))



if __name__ == '__main__':
    graph = Graph('./graph2.txt', undirected=False)
    nodes = graph.nodes

    h = graph.calc_distance
    path = a_star(nodes['10'], nodes['1'], h)
    print(path)

    graph.draw_graph()
    graph.draw_path(path)

    turtle.done()
