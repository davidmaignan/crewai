import sys
from heapq import heappop, heappush

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
distances[start] = 0
    ehq_q = []

    # Initialize ehq_q with nodes and their distances from the start node
    for node in graph:
        if (node != start) and (distances[node] > min([d for n, d in distances.items() if n == node or (n not in graph[start])]) + graph[node][start]):
            heappush(ehq_q, (graph[node][start], node))

    # Perform Dijkstra's algorithm
    while ehq_q:
        (dist, current_node) = heappop(ehq_q)
        for neighbor, neighbor_dist in graph[current_node].items():
            old_cost = distances[neighbor]
            new_cost = dist + neighbor_dist
            if new_cost < old_cost:
                distances[neighbor] = new_cost
                heappush(ehq_q, (new_cost, neighbor))

    return distances
def main():
    graph = {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2, 'D': 5}, 'C': {'A': 4, 'B': 2, 'D': 1}, 'D': {'B': 5, 'C': 1}}
    start_node = 'A'
    result = dijkstra(graph, start_node)
    print(result)

main()