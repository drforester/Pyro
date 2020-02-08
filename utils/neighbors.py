import numpy as np

'''
Returns a list of neighboring point values, out to max_sigma distance from (0,0).
These values will be added to a (y,x) point from a map.
'''
def getAdjacency(max_sigma):
    span = [x for x in range(-(max_sigma), (max_sigma)+1)]
    adjacency = [(i,j) for i in span for j in span if (i,j) != (0,0)]
    return adjacency
