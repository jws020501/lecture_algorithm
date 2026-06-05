class Graph:
    def __init__(self, bidirectional=False):
        num_node, num_edge = map(int, input().split())
        self.graph = [[] for _ in range(num_node + 1)]
        for _ in range(num_edge):
            u, v = map(int, input().split())
            self.graph[u].append(v)
            if bidirectional:
                self.graph[v].append(u)


class DFS:
    def __init__(self, graph, start_node=1):
        self.graph = graph
        self.visited = [False] * len(graph)
        self.start_node = start_node

    def dfs(self, node):
        if not self.visited[node]:
            print(node, end=' ')
            self.visited[node] = True
            for neighbor in self.graph[node]:
                self.dfs(neighbor)
class BFS:
    def __init__(self, graph, start_node=1):
        self.graph = graph
        self.visited = [False] * len(graph)
        self.start_node = start_node

    def bfs(self, node):
        queue = [node]
        self.visited[node] = True
        while queue:
            current = queue.pop(0)
            print(current, end=' ')
            for neighbor in self.graph[current]:
                if not self.visited[neighbor]:
                    queue.append(neighbor)
                    self.visited[neighbor] = True

if __name__ == "__main__":
    is_directed = input(">> 방향성 여부 (y/n): ").lower() == 'y'
    g = Graph(is_directed=='y').graph
    start_node = int(input(">> 시작노드:"))
    print("DFS 탐색 결과:",end=' ')
    DFS(g, start_node).dfs(start_node)
    print("\nBFS 탐색 결과:",end=' ')
    BFS(g, start_node).bfs(start_node)