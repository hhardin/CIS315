import sys
from collections import defaultdict

def add_edge(G, u, v):
	G[u].append(v)
 
def generate_edges(G):
    	edges = []
    	for node in G:
        	for neighbour in G[node]:
            		edges.append((node, neighbour))
    	return edges
 
def find_all_paths(G, u, v, path = []):
	path = path + [u]
	if u == v:
		return [path]
	paths = []
	for node in G[u]:
		if node not in path:
			new_paths = find_all_paths(G, node, v, path)
		for new_path in new_paths:
			paths.append(new_path)
	return paths

def find_shortest_path(G, u, v, path = []):
        path = path + [u]
        if u == v:
            return path
        shortest = None
        for node in G[u]:
            if node not in path:
                new_path = find_shortest_path(G, node, v, path)
                if new_path:
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path
        return shortest

def find_longest_path(G, u, v, path = []):
        path = path + [u]
        if u == v:
            return path
        longest = None
        for node in G[u]:
            if node not in path:
                new_path = find_longest_path(G, node, v, path)
                if new_path:
                    if not longest or len(new_path) > len(longest):
                        longest = new_path
        return longest

def driver():
	num_Gs = int(sys.stdin.readline().strip())
	if num_Gs is 0:
		print(0)
		return
	for i in range(1, num_Gs + 1):
		G = defaultdict(list)
		V = int(sys.stdin.readline().strip())
		E = int(sys.stdin.readline().strip())
		for _ in range(E):
			edges = sys.stdin.readline().strip().split()
			u = edges[0]
			v = edges[1]
			add_edge(G, u, v)
 
		all_paths = len(find_all_paths(G, str(1), str(V)))
		shortest_path = len(find_shortest_path(G, str(1), str(V))) - 1
		longest_path = len(find_longest_path(G, str(1), str(V))) - 1
		print("graph number: ", i)
		print("Shortest path: ", shortest_path)
		print("Longest path: ", longest_path)
		print("Number of paths: ", all_paths)

if __name__ == "__main__":
    driver() 
