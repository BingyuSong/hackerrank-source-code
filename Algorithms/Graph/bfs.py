#!/usr/bin/env python
# -*- coding: utf-8 -*-


def BFS(start, vertices, edges):
    global path
    # if not vertices[start]:
    neighbors = [start]
    # if edges:
    while neighbors:
        v = neighbors.pop()
        vertices[start] = True
        for edge in edges:
            if v in edge:
                index = edge.index(v)
                the_other = edge[1-index]
                if not vertices[the_other]:
                    path[the_other] = path[v]+6
                    neighbors.append(the_other)
                    edges = [_ for _ in edges if _ != edge]

test_cases = int(raw_input())
result = []
if 1 <= test_cases <= 10:
    for i in range(test_cases):
        path = []
        inputs = [int(i) for i in raw_input().strip().split(" ")]
        node_number, edge_number = inputs[0], inputs[1]
        vertices = [False]
        path = [0]
        for i in range(node_number):
            # Mark every vertex as unvisited.
            vertices.append(False)

            # Define the distance between start vertex and others as infinit.
            path.append(99999)
        # If the value if index i is "True", this means vertex i has been
        # visited.

        # The distance between start vertex and itself is 0.
        edges = []
        # contrains
        if 2 <= node_number <= 1000 and 1 <= edge_number <= ((node_number)*((node_number)-1))/2:
            for e in range(edge_number):
                # store all edges in a list.
                edges.append([int(i) for i in raw_input().strip().split(" ")])
        # BFS.
        # result.append(BFS(start, vertices, edges, path))
        start = int(raw_input())
        path[start] = 0
        BFS(start, vertices, edges)
        for v in range(1, node_number+1):
            if path[v] == 99999:
                path[v] = -1
        path = [_ for _ in path if _ != 0]
        result.append(path)

for p in result:
    print str(p)[1:-1].replace(",", "")
