import heapq

def dijkstra(graph, src):
    dist = {v: float('inf') for v in graph}
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('D', 5)],
    'C': [('B', 2), ('D', 5)],
    'D': []
}
print(dijkstra(graph, 'A'))