# from django.shortcuts import render
from django.http import HttpResponse
from re import split as split
# from tree import tree as tr
# from graph import graph as g
import numpy as np
import msvcrt
import json

class edge():

    def __init__(self, first, last, weigth=0):
        self.first = first
        self.last = last
        self.weigth = weigth
        self.key1 = '{first} - {last}'.format(first=self.first, last=self.last)
        self.key2 = '{last} - {first}'.format(first=self.first, last=self.last)

    def doesInclude(self, vertex):
        if (self.first is vertex or self.last is vertex):
            return True
        return False


class tree():
    def __init__(self, p, root=0, fathers=None, weigths=None):
        self.__map = {}
        self.__p = p
        self.__root = root

        if (fathers is not None and weigths is not None):
            l = len(fathers)
            self.__q = l

            for i in range(1, l):
                self.__map[i] = [fathers[i], weigths[i]]
        elif (fathers is not None):
            l = len(fathers)
            self.__q = l
            for i in range(1, l):
                self.__map[i] = [fathers[i], 0]
        else:
            self.__q = 0

    def doesVHaveParent(self, v):
        for i in self.__map:
            if (i == v):
                return True
        return False

    def add(self, v, parent, weigth=0):
        if (v == self.__p):
            self.__p += 1
        elif (v > self.__p):
            self.__p = v

        if (self.doesVHaveParent(v) is False):
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
        while (v != self.__root):
            path.append(self.__map[v][0])
            v = self.__map[v][0]

        return path

    def isLeaf(self, v):
        for i in self.__map:
            if (self.__map[i][0] == v):
                return False
        return True

    def pop(self, leaf):
        if (self.isLeaf(leaf) is True):
            self.__map.pop(leaf)

            self.__q -= 1

    def show(self):
        print(self.__map)


class Graph():

    def __init__(self, p, edges=None, weigths=None):
        self.__p = p
        self.__map = {}

        for i in range(p):
            self.__map[i] = []

        if (weigths is not None and edges is not None):
            l = len(edges)
            for i in range(l):
                self.__map[edges[i][0]].append([edges[i][1], weigths[i]])
                self.__map[edges[i][1]].append([edges[i][0], weigths[i]])
                self.__q = len(edges)
        elif (edges is not None):
            self.__map[edges[i][0]].append([edges[i][1], 0])
            self.__map[edges[i][1]].append([edges[i][0], 0])
            self.__q = len(edges)
        else:
            self.__q = 0

    def add(self, v, u, weigth=0):
        self.__map[v].append([u, weigth])
        self.__map[u].append([v, weigth])
        self.__q += 1

    def remove(self, u, v, weigth=0):
        self.__map[u].remove([v, weigth])
        self.__map[v].remove([u, weigth])
        self.__q -= 1

    def degree(self, v):
        return len(self.__map[v])

    def P(self):
        return self.__p

    def Q(self):
        return self.__q

    def doesEdgeExist(self, v, u):
        for i in self.__map[v]:
            if (i[0] == u):
                return True
        return False

    def weigth(self, v, u):
        for i in self.__map[v]:
            if (i[0] == u):
                return i[1]

    def setWeight(self, v, u, newWeigth, lastWeigth=0):
        self.__map[u].remove([v, lastWeigth])
        self.__map[v].remove([u, lastWeigth])

        self.__map[v].append([u, newWeigth])
        self.__map[u].append([v, newWeigth])

    def neighbors(self, v):
        return self.__map[v]

    def show(self):
        print(self.__map)

    def dijkstra(self, v):
        INF = 10000
        ansTree = tree(p=self.__p, root=v)
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

        while (markCounter != self.__p):
            disMin = INF

            for i in range(self.__p):
                if (dis[i] < disMin and mark[i] is False):
                    disMin = dis[i]
                    vDisMin = i
                    # print('I\'m Here')

            # print(vDisMin)
            mark[vDisMin] = True
            markCounter += 1

            for u in self.neighbors(vDisMin):
                # print(dis[u[0]], dis[vDisMin])
                if (dis[vDisMin] + u[1] < dis[u[0]]):
                    dis[u[0]] = dis[vDisMin] + u[1]
                    # print('Hello')
                    if (ansTree.doesVHaveParent(u[0]) is False):
                        ansTree.add(u[0], vDisMin, u[1])
                    else:
                        # print(u[0])
                        ansTree.pop(u[0])
                        ansTree.add(u[0], vDisMin, u[1])

        return ansTree


def dijkstra(graph, v):
    INF = 10000
    p = graph.P()
    ansTree = tree(p=p, root=v)
    mark = []
    markCounter = 1
    dis = []

    for i in range(p):
        dis.append(INF)
        mark.append(False)

    dis[v] = 0
    disMin = INF
    vDisMin = v
    mark[v] = True

    while (markCounter != p):
        disMin = INF

        for i in range(p):
            if (dis[i] < disMin and mark[i] is False):
                disMin = dis[i]
                vDisMin = i
                # print('I\'m Here')

        # print(vDisMin)
        mark[vDisMin] = True
        markCounter += 1

        for u in graph.neighbors(vDisMin):
            # print(dis[u[0]], dis[vDisMin])
            if (dis[vDisMin] + u[1] < dis[u[0]]):
                dis[u[0]] = dis[vDisMin] + u[1]
                # print('Hello')
                if (ansTree.doesVHaveParent(u[0]) is False):
                    ansTree.add(u[0], vDisMin, u[1])
                else:
                    # print(u[0])
                    ansTree.pop(u[0])
                    ansTree.add(u[0], vDisMin, u[1])

    return ansTree

def index(request):
    u = int(request.GET.get('u', ''))
    v = int(request.GET.get('v', ''))

    p = 11
    q = 17
    graph = Graph(p)

    graph.add(0, 1, 1)
    graph.add(0, 8, 2)
    graph.add(0, 9, 100)
    graph.add(1, 10, 5)
    graph.add(2, 10, 6)
    graph.add(2, 8, 3)
    graph.add(2, 3, 9)
    graph.add(2, 4, 5)
    graph.add(3, 4, 1)
    graph.add(4, 5, 8)
    graph.add(5, 8, 7)
    graph.add(5, 6, 3)
    graph.add(7, 6, 1)
    graph.add(8, 7, 9)
    graph.add(9, 10, 1)
    graph.add(9, 5, 7)
    graph.add(9, 6, 4)

    path = graph.dijkstra(v)
    res = path.climb(u)
    # res = ''
    # for vertextes in path.climb(u):
    #     res += str(vertextes) + ','

    return HttpResponse(json.dumps(res),content_type='application/json')

