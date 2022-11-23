def solution(s, t, path):
    
    #This solution is based on Dignic algorithm
    from collections import deque

    #bredth first search algorithm
    def bfs(source, destination, matrix):
        #Set visited nodes and add source node to stack
        visited = deque([-1 for i in range(len(matrix))])
        visited[source] = source
        stack = deque([source])
        
        while stack:
            node = stack.popleft()
            for i in range(len(matrix)):
                #Check if flow is possible and check if node was visited already.
                if (matrix[node][i][1] - matrix[node][i][0]) != 0 and visited[i] == -1:
                    
                    #If target is reached
                    if i == destination:
                        visited[destination] = node
                        flow = deque([destination])
                        temp = destination
                        
                        while temp != source:
                            #Build flow in reversed order (t->s)
                            temp = visited[temp]
                            flow.append(temp)
                        flow.reverse()
                                                
                        #Get the max flow allowed by capacity
                        e = [matrix[flow[i-1]][flow[i]]  for i in range(1,len(flow))]
                        total = min([abs(x[1])-x[0] for x in e])
                            
                        #Modify matrix
                        #Add flow to flow edge and substract from reversed edge
                        cp = source
                        for j in range(1,len(flow)):    
                            if matrix[cp][flow[j]][1] < 0: 
                                matrix[cp][flow[j]][1] += total
                            else:
                                matrix[cp][flow[j]][0] += total
                            
                            if matrix[flow[j]][cp][1] <= 0: 
                                matrix[flow[j]][cp][1] -= total
                            else:
                                matrix[flow[j]][cp][0] += total                
                            cp = flow[j]
                        
                        return True
                    else:
                        visited[i] = node
                        stack.append(i)
        return False
    
    # Create new matrix with single source and single target
    # Additionally change each value to [current flow, maximal capacity]
    L = len(path)
    mc = sum([j for i in path for j in i])
    G = [[[0,0] for i in range(L+2)] for j in range(L+2)]
    
    #Fill values from path
    for i in range(L):
        for j in range(L):
            G[i+1][j+1] = [0,path[i][j]]
    
    #Apply max capacity
    for i in s:
        G[0][i+1] = [0,mc]
    for i in t:
        G[i+1][-1] = [0,mc]

    # Do BFS
    while bfs(0, len(G)-1,G):
        # G is being modified inside bfs function
        pass 
    max_flow = sum([G[0][i][0] for i in range(len(G))])
    
    return max_flow