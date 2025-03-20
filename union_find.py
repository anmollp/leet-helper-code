class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int):
        p1, p2 = self.find(x), self.find(y)
        if p1 != p2:
            if self.size[p1] > self.size[p2]:
                self.parent[p2] = x
                self.size[p1] += self.size[p2]
            else:
                self.parent[p1] = y
                self.size[p2] += self.size[p1]
            return True
        return False
