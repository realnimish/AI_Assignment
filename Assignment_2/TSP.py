'''
    TSP using A* Search
'''

class state:

    def __init__(self):
        self.g = 0
        self.h = 0
        self.visited = []
        self.unvisited = []

    def init(self, size, start = 0):
        self.visited = [start]
        self.unvisited = [i for i in xrange(size) if i != start]

    def f(self):
        return self.g + self.h

    def cost(self, graph):
        if len(self.visited) == 0: return -1
        return self.g + graph[ self.visited[0] ][ self.visited[-1] ]

    def getState(self,parent):
        self.visited = list(parent.visited)
        self.unvisited = list(parent.unvisited)


def main():
    n = int(raw_input("Enter number of nodes : "))
    graph = [ [0]*n for i in xrange(n)]

    for i in xrange(n):
        for j in xrange(i+1,n):
            graph[i][j] = int(raw_input("Edge Cost of %d-%d  : "%(i+1,j+1)))
            graph[j][i] = graph[i][j]

    sol = solve(n,graph)
    print 'Path : ',
    print '->'.join(map(str,sol.visited + [sol.visited[0]]))
    print 'Cost : ',sol.cost(graph)

def mst(arr,graph):
    return 1

def solve(n,graph):
    initial = state()
    initial.init(n)
    initial.h = mst( [i for i in xrange(n)] ,graph)
    
    Q = [ (initial.f(),initial) ]  # Make it priority queue
    solution = None
    
    while Q:
        f,curState = Q.pop(0)
        if curState.unvisited == []:
            if solution is None:
                solution = curState
            elif curState.cost(graph) < solution.cost(graph):
                solution = curState
        else:
        
            X = mst(curState.unvisited, graph)

            for i in xrange( len(curState.unvisited) ):
                nextState = state()
                nextState.getState(curState)
                nextState.visited.append( nextState.unvisited.pop(i) )
                nextState.g = curState.g + graph[ curState.visited[-1] ][ curState.unvisited[i] ]
                nextState.h = X
                Q.append((nextState.f(),nextState))
    return solution


# Driver Code
main()


        
