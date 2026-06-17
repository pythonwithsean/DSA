import heapq

#infinity
infinity = float("inf")

def makeGraph(): 
	#Graph has to be weighted for this to work
	# tuple = (cost, to_node)
    return {
        'A': [(4, 'B'), (2, 'C')],
        'B': [(3, 'C'), (3, 'E'), (2, 'D')],
        'C': [(1, 'B'), (4, 'D'), (5, 'E')],
        'D': [],
        'E': [(1, 'D')],
    }


#implementation with Heap
def dijkstras(graph, start): 
	shortestPaths = {}
	visited = set()
	heap = []
	#initially all the nodes are set to infinity
	for node in graph.keys(): 
		shortestPaths[node] = infinity
	# initially we start at the start and the distance from ourself is 0
	shortestPaths[start] = 0
	# Since we start at the start we add it to our visited
	visited.add(start)
	heapq.heappush(heap,(0,start))
	# While the heap has a node we perform BFS
	while heap: 
		(distance, node) = heapq.heappop(heap)
		# we traverse this node
		visited.add(node)
		# We go through all our neighbours
		for edge in graph[node]: 
			cost, to_node = edge
			if(to_node not in visited) and (distance + cost < shortestPaths[to_node]):
				shortestPaths[to_node] = distance + cost
				heapq.heappush(heap,(shortestPaths[to_node],to_node))	

	return shortestPaths
	
if __name__ == "__main__": 
	graph = makeGraph()
	start = 'A'
	result = dijkstras(graph,start)
	print(result)