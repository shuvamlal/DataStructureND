import math
from queue import PriorityQueue

def heuristic_distance(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2)) # distance between two points

def create_route(prev, start, goal):
    current_node = goal 
    route = [current_node]
    while current_node != start: # moving towards goal to start
        current_node = prev[current_node]
        route.append(current_node)
    route.reverse() # reversing the route
    return route
    return

def shortest_path(route, start, goal):
    route_queue = PriorityQueue()
    route_queue.put(start, 0)
    
    prev = {start: None} 
    cost = {start: 0} 

    while not route_queue.empty():
        current_node = route_queue.get()

        if current_node == goal:
            create_route(prev, start, goal)

        for node in route.roads[current_node]:
            new_cost = cost[current_node] + heuristic_distance(route.intersections[current_node], route.intersections[node]) 
            
            if node not in cost or new_cost < cost[node]:               
                cost[node] = new_cost
                total_cost = new_cost + heuristic_distance(route.intersections[current_node], route.intersections[node])
                
                route_queue.put(node, total_cost)
                prev[node] = current_node # stores the cost efficient route node

    return create_route(prev, start, goal)
