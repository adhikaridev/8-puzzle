class state:


    def __init__(self):
        self._parent = [[0, 2, 5, 3, 4, 1, 6, 7, 8]]
        print self._parent

    def upswitch(self):
        self.parent = current_node[:]
        self.parent[p] = self.parent[p - 3]  # switching with up
        self.parent[p - 3] = 0
    def downchild(self):
        self.parent = current_node[:]
        self.parent[p] = self.parent[p - 3]  # switching with up
        self.parent[p - 3] = 0



state1 = state()
