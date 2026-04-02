def kruskal(edges: list) -> list:
    """
    kruskal - function for finding the minimum spanning tree for weighted connected undirected graph.

    :param edges: List of edges represented as tuple(a, b, weight)
    :return: List of edges in the minimum spanning tree.
    """
    # Sorting input edges by weight
    edges = sorted(edges, key=lambda item: item[2])
    # Adding first edge (with smallest weight) to result list and deleting it from input edges.
    result = [edges.pop(0)]
    # Adding to array first set of expanded points.
    array = [{result[0][0], result[0][1]}]

    # For each edge in sorted list (without deleted first)
    for edge in edges:
        # Looking for start point occurrences in expanded points sets and trying to get set index.
        start_connection = next(iter([i for i in range(len(array)) if edge[0] in array[i]]), None)
        # Looking for end point occurrences in expanded points sets and trying to get set index.
        end_connection = next(iter([i for i in range(len(array)) if edge[1] in array[i]]), None)

        # If edge makes cycle - skip it.
        if start_connection is not None and start_connection == end_connection:
            continue

        # Adding edge to result list.
        result.append(edge)
        # If edge first point found in expanded points set - add second edge point.
        if start_connection is not None:
            array[start_connection].add(edge[1])
        # If edge second point found in expanded points set - add first edge point.
        if end_connection is not None:
            array[end_connection].add(edge[0])

        # If edge is not connected with any chains - add new set of expanded points. (new chain)
        if start_connection is None and end_connection is None:
            array.append({edge[0], edge[1]})

        # If edge connects two chains - merge these chains. (union from two expanded points sets)
        if start_connection is not None and end_connection is not None:
            array.append(array[start_connection].union(array[end_connection]))
            array = [array[i] for i in range(len(array)) if i != start_connection and i != end_connection]

    return result
################################################################################
import numpy as np
import csv
################################################################################
def process_file():
    filename = '107_network.txt'
    #filename = '107_example.txt'
    lst = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        row = 0
        for line in reader:
            col = 0
            for element in line:
                if element.isnumeric():
                    edge = [str(row),str(col),int(element)]                
                    lst.append(edge)
                col += 1
            row += 1       

    return lst
################################################################################

EDGES = process_file()
result = kruskal(EDGES)
total = 0
for element in result:
    total += element[2]

print(total)
