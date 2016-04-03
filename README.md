# Khan-Academy-Project

## Requirements
Please make sure to download the dependencies needed in order to run the file. 
- Python (at least 2.7)
- networkx and matplotlib, install by running 'pip install networkx matplotlib'

## How to run
There are 4 different modes that you can run the program with.
* Total Infections
	* To run Total Infections on a randomly generated graph with visualization, execute the following command, `python infection.py -r total_infection NUMBER_OF_NODES NUMBER_OF_EDGES`, where `NUMBER_OF_NODES` is the desired number of nodes and `NUMBER_OF_EDGES` is the desired number of edges you want in this randomly generated graph. The initial infection starting node will be chosen arbitrarily and a graph will be shown to display the infection.
	* To run Total Infections on a designated user-implemented graph file, execute the following command, `python infection.py total_infection FILE_NAME`, where `FILE_NAME` is the name of the file of the custom graph.
* Limited Infections
	* To run Limited Infections on a randomly generated graph with visualization, execute the following command, `python infection.py -r limited_infection NUMBER_OF_NODES NUMBER_OF_EDGES NUMBER_OF_NODES_INFECTED`, where `NUMBER_OF_NODES` is the desired number of nodes and `NUMBER_OF_EDGES` is the desired number of edges and `NUMBER_OF_NODES_INFECTED` is the number of nodes you want infected in this randomly generated graph. Limited Infections will try to get as close as possible to `NUMBER_OF_NODES_INFECTED` as possible if that infection is impossible.
	* To run Limited Infections on a designated user-implemented graph file, execute the following command, `python infection.py limited_infection FILE_NAME`, where `FILE_NAME` is the name of the file of the custom graph.