def dfs(graph, node, visited = None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end = " ")
    for nbr in graph[node]:
        if nbr not in visited:
            dfs(graph, nbr, visited)

graph = {
    0: [1, 2],
    1: [2, 3],
    2: [3, 4],
    3: [4, 0],
    4: [1]
}
dfs(graph, 1)