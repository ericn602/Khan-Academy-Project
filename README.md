# Khan-Academy-Project

## Requirements
Please make sure to download the dependencies needed in order to run the file. 
- Python (at least 2.7)
- networkx and matplotlib, install by running `pip install networkx matplotlib`

## How to run
There are 4 different modes that you can run the program with.
* Total Infections
	* To run Total Infections on a randomly generated graph with visualization, execute the following command, `python infection.py -r total_infection NUMBER_OF_NODES NUMBER_OF_EDGES`, where `NUMBER_OF_NODES` is the desired number of nodes and `NUMBER_OF_EDGES` is the desired number of edges you want in this randomly generated graph. The initial infection starting node will be chosen arbitrarily and a graph will be shown to display the infection.
	* To run Total Infections on a designated user-implemented graph file, execute the following command, `python infection.py total_infection FILE_NAME`, where `FILE_NAME` is the name of the file of the custom graph.
* Limited Infections
	* To run Limited Infections on a randomly generated graph with visualization, execute the following command, `python infection.py -r limited_infection NUMBER_OF_NODES NUMBER_OF_EDGES NUMBER_OF_NODES_INFECTED`, where `NUMBER_OF_NODES` is the desired number of nodes and `NUMBER_OF_EDGES` is the desired number of edges and `NUMBER_OF_NODES_INFECTED` is the number of nodes you want infected in this randomly generated graph. Limited Infections will try to get as close as possible to `NUMBER_OF_NODES_INFECTED` as possible if that infection is impossible.
	* To run Limited Infections on a designated user-implemented graph file, execute the following command, `python infection.py limited_infection FILE_NAME`, where `FILE_NAME` is the name of the file of the custom graph.
* In both instances, red nodes will represent the infected nodes.
## How to create a custom graph file
```
NUMBER_OF_NODES
EDGE1
EDGE2
.
.
.
PARAMETER
```
In this `NUMBER_OF_NODES` is the number of nodes that you want in the graph. Nodes will have numerical labels from 1 to `NUMBER_OF_NODES`.
`EDGE#` will represent one edge that you want to add. `2,3` will create an edge between nodes 2 and 3. `PARAMETER`, in Total Infection Mode, is the starting infected node that you want to specify. `PARAMETER`, in Limited Infection Mode, is how many nodes you want to infect.
For Example, the file
```
10
1,2
2,3
3,4
4
```
will create 10 nodes, with edges between 1,2 2,3 3,4. In Total Infection mode, the starting infected node will be node 4. In Limited Infection mode, we will try to infect exactly 4 nodes if possible.

## Overview of the project
* Total Infections
	* Implementation Total Infections was fairly simple. We know that given a starting node, to find its connected component, we can simply run DFS or BFS. In our case, BFS was used in order to find the connected component of our starting node.
* Limited Infections
	* I interpreted Limit Infections as the following. Given the number of nodes we want to infect, try to infect that many nodes and if impossible, try to infect as many nodes as possible up to the number of nodes we want to infect. In a way, the given number of nodes is the upper bounds on how many nodes we can infect.
	* We can utilize that fact that when we infect a node, we basically infect its whole connect components. If we didn't do this, then there would always be a violation where a coach and a student aren't utilizing the same site.
	* Knowing this, our goal is to basically find all connected components such that the sum of nodes in these connected components is equal to or less than the desire number of nodes we want to infect.
	* This problem can be model using the Knapsack problem, taught in CS 170 at UC Berkeley for me. If you would like more information on the Knapsack problem, please check out the book used for CS 170 at http://beust.com/algorithms.pdf. Page 172 has information regarding the Knapsack problem.
	* However there is a downside to using Dynamic Programming in order to find the infected nodes. We know that the runtime of the Knapsack algorithm is O(nW), where, in our case, W is the number of nodes we want to infect. Knapsack is an NP-Complete problem, since W can be arbitrarily big. Thus, although this solution is elegant, it probably won't scale too well as the number of desired infections skyrockets.

## Feedback

Thank you for allowing me an attempt at completing this challenge. I've never had an project-based interview before and I have to say that the level of freedom given upon the interpretation of Limited Infections gave me the opportunity to model the problem using what I've learned fairly recently. Khan Academy's proclivity towards project based interviews really gave me the ability to tackle a problem that I'd consider to be more realistic than typical interview questions. I appreciate the time and look forward to hearing from you again in the future. Feel free to contact me at enguyen@berkeley.edu for any further questions.

