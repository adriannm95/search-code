# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)


print "En Anchura -----> ",search.breadth_first_graph_search(ab).path()
print "En Profundidad ----> ",search.depth_first_graph_search(ab).path()
print "Rama coste Subestimacion ---->",search.rama_tree_search(ab).path()

#coste de la ruta mas la heuristica nodo actual hasta el que quiero llegar + el pathcost

#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
