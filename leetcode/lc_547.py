class DSU:

    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.components = n

    def union(self,a,b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return False

        self.components -= 1

        if self.size[pb] > self.size[pa]:
            self.parent[pa] = pb
            self.size[pb] += self.size[pa]
            self.size[pa] = 0
        else:
            self.parent[pb] = pa
            self.size[pa] += self.size[pb]
            self.size[pb] = 0

        return True

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """

                0
               /
              1                3
             /
            2

            union(2,3)

            find(2)
                parent[2] = find(parent(1)) 0
                    find(1)
                        parent[1] = find(parent(1)) 0
                            find(0)
                                return 0


        """
        N = len(isConnected)
        ds = DSU(N)
        res = 0
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if isConnected[i][j]:
                    ok = ds.union(i,j)

        return ds.components
