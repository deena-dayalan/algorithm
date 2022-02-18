# PUSH-RELABEL (Tested using CLRS example)
import math

def MaxFlow(capacity, source, sink):
    
    # nodes is number of vertices
    nodes = len(capacity) 
    
    # initiating flow in edges [nodes]x[nodes] matrix
     
    flow = []
    x = []
    for i in range(nodes):
        for i in range(nodes):
            x.append(0)
        flow.append(x)
        x = []
     
    # Initializing height for each node
    height = [0] * nodes 
     
    # Initializing exces flow in each node
    excess_flow = [0] * nodes 
     
    # Initializing list for each node visited in relabel
    visits   = [0] * nodes 
     
    # List of nodes excluding source and sink
    other_nodes = []
    for i in range(nodes):
        if i!=source and i!=sink:
            other_nodes.append(i)
    
    # To push excess flow from one end of edge to other
    def PUSH(start,end):

        new_flow = min(excess_flow[start],capacity[start][end] - flow[start][end])
        flow[start][end] += new_flow
        excess_flow[start] -= new_flow
        excess_flow[end] += new_flow
        flow[end][start] -= new_flow
    
    # Increasing height of start compared to its neighbour which has least height
    def RELABEL(start):
        
        minimum_height = math.inf
        for end in range(nodes):
            if capacity[start][end]-flow[start][end] > 0:
                minimum_height = min(minimum_height,height[end])
                height[start] = minimum_height + 1
                
    # Checking for perfect neighbour 
    def MAKE_FLOW(start):
        while excess_flow[start] > 0:
            if visits[start] < nodes: 
                end = visits[start]
                if capacity[start][end]-flow[start][end] > 0 and height[start] > height[end]:
                    PUSH(start,end)
                else:
                    visits[start] +=1
            else:
                RELABEL(start)
                visits[start] = 0
                
    # Setting heights for source and sink, excess flow of source as inf
    
    height[source] = nodes
    excess_flow[source] = math.inf
    
    # PUSHING to the neighbours of source
    for end in range(nodes):
        if capacity[source][end] > 0:
            PUSH(source,end)
    
    pointer = 0
    while pointer < len(other_nodes):
        start = other_nodes[pointer]
        previous_height = height[start]
        MAKE_FLOW(start)
        if height[start] > previous_height:
            other_nodes.insert(0, other_nodes.pop(pointer))
            pointer = 0
        else:
            pointer += 1
    print('The flow matrix is \n')
    for i in range(len(flow)):
        print(flow[i][:])

    return sum(flow[source][:])

###############################################################################

source = 0
sink = 5

capacity = [[ 0, 16, 13,  0,  0,  0 ],  
            [ 0,  0,  0, 12,  0,  0 ],  
            [ 0,  4,  0,  0, 14,  0 ],  
            [ 0,  0,  9,  0,  0, 20 ],  
            [ 0,  0,  0,  7,  0,  4 ],  
            [ 0,  0,  0,  0,  0,  0 ]]  
    

print ('\n' + "Maximum flow value :",MaxFlow(capacity, source, sink))