class tree():
    def __init__(self, p, root = 0, fathers = None, weigths = None):
        self.__map = {}
        self.__p = p
        self.__root = root
       
        if(fathers is not None and weigths is not None):
            l = len(fathers)
            self.__q = l

            for i in range(1, l):
                self.__map[i] = [fathers[i], weigths[i]]
        elif(fathers is not None):
            l = len(fathers)
            self.__q = l
            for i in range(1, l):
                self.__map[i] = [fathers[i] , 0]
        else:
            self.__q = 0

    def doesVHaveParent(self, v):
        for i in self.__map:
            if(i == v):
                return True
        return False

    
    def add(self, v, parent ,weigth = 0):
        if(v == self.__p):
            self.__p += 1
        elif(v > self.__p):
            self.__p = v

        if(self.doesVHaveParent(v) is False):
            self.__map[v] = [parent, weigth]
            self.__q += 1

    def P(self):
        return self.__p

    def Q(self):
        return self.__q

    def root(self):
        return self.__root

    def climb(self, child):
        path = [child]
        v = child
        while(v != self.__root):
            path.append(self.__map[v][0])
            v = self.__map[v][0]
            
        return path

    def isLeaf(self, v):
        for i in self.__map:
            if(self.__map[i][0] == v):
                return False
        return True

    def pop(self, leaf):
        if(self.isLeaf(leaf) is True):
            self.__map.pop(leaf)

            self.__q -= 1    

    def show(self):
        print(self.__map)