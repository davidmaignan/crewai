from collections import deque
def breadth_first_search(graph, root):
    visited = set()
    queue = deque([root])

    while queue:
        vertex = queue.popleft()

        print(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

graph = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
breadth_first_search(graph, 'A')