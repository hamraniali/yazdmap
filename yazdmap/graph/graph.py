from tree import tree as tr

class graph():
    
    def __init__(self, p, edges = None, weigths= None):
        self.__p = p
        self.__map = {}

        for i in range(p):
            self.__map[i] = []

        if(weigths is  not None and edges is not None):
            l = len(edges)
            for i in range(l):
                self.__map[edges[i][0]].append([edges[i][1] , weigths[i]])
                self.__map[edges[i][1]].append([edges[i][0] , weigths[i]])
                self.__q = len(edges)
        elif(edges is not None):
            self.__map[edges[i][0]].append([edges[i][1] , 0])
            self.__map[edges[i][1]].append([edges[i][0] , 0])
            self.__q = len(edges)
        else:
            self.__q = 0

    def add(self, v, u, weigth = 0):
        self.__map[v].append([u , weigth])
        self.__map[u].append([v , weigth])
        self.__q += 1

    def remove(self, u, v , weigth = 0):
        self.__map[u].remove([v , weigth])
        self.__map[v].remove([u , weigth])
        self.__q -= 1

    def degree(self, v):
        return len(self.__map[v])

    def P(self):
        return self.__p
    
    def Q(self):
        return self.__q

    def doesEdgeExist(self, v, u):
        for i in self.__map[v]:
            if(i[0] == u):
                return True
        return False

    def weigth(self, v, u):
        for i in self.__map[v]:
            if(i[0] == u):
                return i[1]

    def setWeight(self, v, u, newWeigth, lastWeigth = 0):
        self.__map[u].remove([v , lastWeigth])
        self.__map[v].remove([u , lastWeigth])

        self.__map[v].append([u , newWeigth])
        self.__map[u].append([v , newWeigth])

    def neighbors(self, v):
        return self.__map[v]

    def show(self):
        print(self.__map)

    def dijkstra(self, v):
        INF = 10000
        ansTree = tr(p = self.__p , root = v)
        mark = []
        markCounter = 1
        dis = []


        for i in range(self.__p):
            dis.append(INF)
            mark.append(False)
        
        dis[v] = 0
        disMin = INF
        vDisMin = v
        mark[v] = True

        while(markCounter != self.__p):
            disMin = INF
            
            for i in range(self.__p):
                if(dis[i] < disMin and mark[i] is False):
                    disMin = dis[i]
                    vDisMin = i
                    # print('I\'m Here')

            # print(vDisMin)
            mark[vDisMin] = True
            markCounter += 1

            for u in self.neighbors(vDisMin):
                # print(dis[u[0]], dis[vDisMin])
                if(dis[vDisMin] + u[1] < dis[u[0]]):
                    dis[u[0]] = dis[vDisMin] + u[1] 
                    # print('Hello')
                    if(ansTree.doesVHaveParent(u[0]) is False):
                        ansTree.add(u[0] , vDisMin , u[1])
                    else:
                        # print(u[0])
                        ansTree.pop(u[0])
                        ansTree.add(u[0] , vDisMin , u[1])

        return ansTree