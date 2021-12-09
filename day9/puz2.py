import numpy as np
import puz1 as help

def bfs(visited, graph, node):
    queue = [get_neighbours(graph, node)]
    output = []

    while queue:
        m = queue.pop(0)
        for neighbour in m:
            if neighbour not in visited:
                visited.append(neighbour)
                if graph[neighbour[0]][neighbour[1]] != 9:
                    output.append(neighbour)
                    queue.append(get_neighbours(graph, neighbour))
    return output

def get_neighbours(array, node):
    i, n = node
    if i == 0:
        if n == 0:
            return (i, n), (i+1, n), (i, n+1)
        elif n == len(array[0])-1:
            return (i, n), (i+1, n), (i, n-1)
        else:
            return (i, n), (i+1, n), (i, n+1), (i, n-1)
    elif i == len(array)-1:
        if n == 0:
            return (i, n), (i-1, n), (i, n+1)
        elif n == len(array[0])-1:
            return (i, n), (i-1, n), (i, n-1)
        else:
            return (i, n), (i-1, n), (i, n+1), (i, n-1)
    else:
        if n == 0:
            return (i, n), (i+1, n), (i-1, n), (i, n+1)
        elif n == len(array[0]) - 1:
            return (i, n), (i+1, n), (i-1, n), (i, n-1)
        else:
            return (i, n), (i+1, n), (i-1, n), (i, n+1), (i, n-1)


def solve_9_2():
    file = open("input9.txt")
    lines = file.readlines()
    tubes = []
    for line in lines:
        tubes += [[x for x in line.strip()]]
    tubes = np.array(tubes, dtype=int)
    tubes.reshape((len(tubes), len(tubes[0])))
    #print(non_adjacent(tubes))
    print(tubes)
    result = 1
    results = []
    for index in help.find_adjacent(tubes):
        results.append(bfs([], tubes, index))
    results.sort(key=len, reverse=True)
    for r in range(3):
        result *= len(results[r])
    return result

if __name__ == '__main__':
    print(solve_9_2())