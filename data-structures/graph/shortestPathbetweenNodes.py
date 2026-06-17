import collections
def createGraph(): 
	# Graph needs to be directed without cycles
	return { 
		'1': ['2','4'],
		'2': ['5'],
		'3': ['2','6'],
		'4': [],
		'5': ['3','6','7'],
		'6': ['8'],
		'7': [],
		'8': ['5','7'],	
	}


def shortestPath(graph, start, end, predecessors):
	queue = collections.deque([start])
	while queue: 
		current = queue.popleft()
		for neighbor in graph[current]: 
			if neighbor == end: 
				predecessors[neighbor] = current
				return predecessors
			if predecessors.get(neighbor) == None: 
				predecessors[neighbor] = current
				queue.append(neighbor)
	return predecessors


if __name__ == "__main__": 
	graph = createGraph()
	start = '1'
	end = '8'
	predecessors = {start: None}
	shortestPath(graph, start, end,predecessors)
	current = end
	result = collections.deque([])
	while predecessors[current] != None: 
		result.appendleft(current)
		current = predecessors[current]
	result.appendleft(current)
	print(list(result))
