import numpy as np
from typing import List
from collections import deque

#yikes me bad https://www.geeksforgeeks.org/print-paths-given-source-destination-using-bfs/
def is_not_visited(x: int, path: List[int]) -> int:
    size = len(path)
    for i in range(size):
        if path[i] == x:
            return 0

    return 1

#yikers https://www.geeksforgeeks.org/print-paths-given-source-destination-using-bfs/
def find_paths(g: List[List[int]], src: int,
              dst: int, v: int) -> None:
    q = deque()
    path = [src]
    q.append(path.copy())

    output = []

    while q:
        path = q.popleft()
        last = path[len(path) - 1]

        if last == dst:
             output += [path]

        for i in range(len(g[last])):
            if is_not_visited(g[last][i], path) or g[last][i].isupper():
                newpath = path.copy()
                newpath.append(g[last][i])
                q.append(newpath)
    return output

def solve_12_1():
    file = open("input12.txt")
    lines = file.readlines()
    graph = {}
    for line in lines:
        line = line.strip()
        line = line.split("-")
        if not line[0] in graph.keys():
            graph[line[0]] = [line[1]]
        else:
            graph[line[0]] += [line[1]]
        if not line[1] in graph.keys():
            graph[line[1]] = [line[0]]
        else:
            graph[line[1]] += [line[0]]
    print(graph)
    return len(find_paths(graph, 'start', 'end', len(graph.keys())))

if __name__ == '__main__':
    print(solve_12_1())