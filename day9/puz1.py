import numpy as np

def find_adjacent(array):
    indexes = []
    for i in range(len(array)):
        for n in range(len(array[i])):
            if i == 0:
                if n == 0:
                    if array[i+1][n] > array[i][n] and array[i][n+1] > array[i][n]:
                        indexes += [(i,n)]
                elif n == len(array[0])-1:
                    if array[i+1][n] > array[i][n] and array[i][n-1] > array[i][n]:
                        indexes += [(i,n)]
                else:
                    if array[i+1][n] > array[i][n] and array[i][n-1] > array[i][n] and array[i][n+1] > array[i][n]:
                        indexes += [(i,n)]
            elif i == len(array)-1:
                if n == 0:
                    if array[i-1][n] > array[i][n] and array[i][n+1] > array[i][n]:
                        indexes += [(i,n)]
                elif n == len(array[0])-1:
                    if array[i-1][n] > array[i][n] and array[i][n-1] > array[i][n]:
                        indexes += [(i,n)]
                else:
                    if array[i-1][n] > array[i][n] and array[i][n-1] > array[i][n] and array[i][n+1] > array[i][n]:
                        indexes += [(i,n)]
            else:
                if n == 0:
                    if array[i+1][n] > array[i][n] and array[i-1][n] > array[i][n] and array[i][n+1] > array[i][n]:
                        indexes += [(i,n)]
                elif n == len(array[0])-1:
                    if array[i+1][n] > array[i][n] and array[i-1][n] > array[i][n] and array[i][n-1] > array[i][n]:
                        indexes += [(i,n)]
                elif array[i - 1][n] > array[i][n] and array[i][n - 1] > array[i][n] \
                    and array[i + 1][n] > array[i][n] and array[i][n + 1] > array[i][n]:
                    indexes += [(i, n)]
    return indexes

def solve_9_1():
    file = open("input9.txt")
    lines = file.readlines()
    tubes = []
    for line in lines:
        tubes += [[x for x in line.strip()]]
    tubes = np.array(tubes)
    tubes.reshape((len(tubes), len(tubes[0])))
    indexes = find_adjacent(tubes)
    result = 0
    for i in indexes:
        result += int(tubes[i[0]][i[1]])+1
    return result

if __name__ == '__main__':
    print(solve_9_1())