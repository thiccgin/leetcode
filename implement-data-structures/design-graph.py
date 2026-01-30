class Graph:
    
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dst not in self.adj_list:
            self.adj_list[dst] = []
        if dst not in self.adj_list[src]:
            self.adj_list[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list:
            return False
        if dst not in self.adj_list[src]:
            return False

        self.adj_list[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        queue = collections.deque()
        queue.append(src)
        visited.add(src)

        while queue:
            node = queue.popleft()
            if node == dst:
                return True

            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return False



