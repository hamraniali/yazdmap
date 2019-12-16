from tree import tree as tr

def dijkstra(graph, v):
    INF = 10000
    p = graph.P()
    ansTree = tr(p = p , root = v)
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

    while(markCounter != p):
        disMin = INF
        
        for i in range(p):
            if(dis[i] < disMin and mark[i] is False):
                disMin = dis[i]
                vDisMin = i
                # print('I\'m Here')

        # print(vDisMin)
        mark[vDisMin] = True
        markCounter += 1

        for u in graph.neighbors(vDisMin):
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