import networkx as nx
import matplotlib.pyplot as plt
import random
import sys

def make_random_graph(num_nodes, num_edges):
	"""
	Helper method that returns a randomly created graph G with num_nodes
	nodes and approximately num_edges edges.
	"""
	G = nx.Graph()
	G.add_nodes_from([i for i in range(1,num_nodes + 1)], infected = 'false')
	edges = []
	for i in range(num_edges):
		while True:
			a = random.randint(1,num_nodes)
			b = random.randint(1,num_nodes)
			if a != b:
				break;
		if (a,b) not in edges:
			edges.append((a,b))
	G.add_edges_from(edges)
	return G
def generate_custom_graph(input_file):
	"""
	Helper method used to generate a graph using an input file.
	"""
	f = open(input_file, 'r')
	i = 0
	edges = []
	param = None
	num_nodes = int(f.readline())
	for line in f:
		if ',' not in line:
			param = int(line)
			break;
		edges.append(tuple(map(int,line.split(','))))
		i = i + 1
	G = nx.Graph()
	G.add_nodes_from([i for i in range(1,num_nodes + 1)], infected = 'false')
	G.add_edges_from(edges)
	f.close()
	return G, param
def total_infection_random(num_nodes, num_edges):
	"""
	Runs the random total infection mode with a randomly created graph with
	num_nodes nodes and num_edges edges. The starting node for this mode is
	arbitrary.
	"""
	G = make_random_graph(num_nodes, num_edges)
	random_node = random.randint(1, num_nodes)
	connected_component = total_infection(G, random_node)
	print '\nStarting node: ' + str(random_node)
	print 'The following nodes are infected: '
	print connected_component
	graph_visualization(G)


def limited_infection_random(num_nodes,num_edges, num_infected):
	"""
	Runs the random total infection mode with a randomly created graph with
	num_nodes nodes and num_edges edges. We want to try to infect num_infected
	nodes. If not possible, then we will try to affect as many nodes as we can.
	"""
	G = make_random_graph(num_nodes, num_edges)
	num_infected_nodes, infected_nodes = limited_infection(G, num_infected)
	if num_infected == num_infected_nodes:
		print '\nWe successfully infected the number of requested nodes!'
	else:
		print '\nWe did not successfully infect the number of requested node, but we did infect ' + str(num_infected_nodes)
	print 'The following nodes are infected: '
	print infected_nodes
	graph_visualization(G)

def graph_visualization(G):
	"""
	Helper method used to plot and visualize the graph G.
	"""
	infected = []
	not_infected = []
	pos=nx.random_layout(G)
	for node in G.nodes():
		if G.node[node]['infected'] == True:
			infected.append(node)
		else:
			not_infected.append(node)
	labels = {}
	for i in range(1, G.number_of_nodes() + 1):
		labels[i] = str(i)
	nx.draw_networkx_nodes(G,pos, nodelist = infected, node_color = 'r', node_size = 200, alpha = 0.8)
	nx.draw_networkx_nodes(G,pos, nodelist = not_infected, node_color = 'b', node_size = 200, alpha = 0.8)
	nx.draw_networkx_edges(G,pos)
	nx.draw_networkx_labels(G, pos, labels, font_size=12)
	plt.show()

def total_infection(G, node):
	"""
	Given a graph G and a starting node, find its connected component.
	This is accomplished by using a simple breadth-first search.
	"""
	connected_component = bfs_infect(G, node)
	for node in connected_component:
		G.node[node]['infected'] = True
	return connected_component

def limited_infection(G, num):
	"""
	Given a graph G and num nodes we want to infect, return the 
	number of nodes we infected as well as the list of nodes infected.
	We basically model the problem after the knapsack problem and use DP
	in order to find the solution.
	"""
	connected_components = [[]]
	visited = []
	for node in G.nodes():
		if node in visited:
			continue
		connected_component = bfs_infect(G, node)
		connected_components.append(connected_component)
		visited = visited + connected_component

	k = [[0 for j in range(len(connected_components))] for w in range(num + 1)]

	for j in range(1, len(connected_components)):
		for w in range(1,len(k)):
			if len(connected_components[j]) > w:
				k[w][j] = k[w][j-1]
			else:
				k[w][j] = max(k[w][j-1],k[w-len(connected_components[j])][j-1] + len(connected_components[j]))
	num_infected_nodes = k[w][j]
	cc_indices = []
	while w >= 0 and j >= 0:
		if w - len(connected_components[j]) < 0:
			break;
		if k[w][j] == k[w-len(connected_components[j])][j-1] + len(connected_components[j]):
			cc_indices.append(j)
			w = w - len(connected_components[j])
		j = j - 1
	
	infected_nodes = []

	for index in cc_indices:
		for node in connected_components[index]:
			G.node[node]['infected'] = True
			infected_nodes.append(node)

	return num_infected_nodes, infected_nodes

def bfs_infect(G, node):
	"""
	Simple bfs implementation
	"""
	stack = [node]
	visited = []
	while len(stack) > 0:
		currentNode = stack.pop(0)
		if currentNode not in visited:
			visited.append(currentNode)
			for neighbor in G.neighbors(currentNode):
				stack.append(neighbor)
	return visited


def main(argv):
	if argv[0] == 'total_infection':
		if argv[1] == '-r':
			total_infection_random(int(argv[2]),int(argv[3]))
		else:
			G, param = generate_custom_graph(argv[1])
			connected_component = total_infection(G, param)
			print '\nStarting node: ' + str(param)
			print 'The following nodes are infected: '
			print connected_component
			graph_visualization(G)

	elif argv[0] == 'limited_infection':
		if argv[1] == '-r':
			limited_infection_random(int(argv[2]),int(argv[3]), int(argv[4]))
		else:
			G, param = generate_custom_graph(argv[1])
			num_infected_nodes, infected_nodes = limited_infection(G, param)
			if param == num_infected_nodes:
				print '\nWe successfully infected the number of requested nodes!'
			else:
				print '\nWe did not successfully infect the number of requested node, but we did infect ' + str(num_infected_nodes)
			print 'The following nodes are infected: '
			print infected_nodes
			graph_visualization(G)

if __name__ == "__main__":
   main(sys.argv[1:])

