import sys

total_dead_ends = 0
dead_ends_list = []
locations = 0
streets = 0
streetsList = []
connections_matrix = []


def connections(l, s):
    global connections_matrix
    connections_matrix = [[0 for i in range(l + 1)] for j in range(l + 1)]
    for street in s:
        v = street[0]
        w = street[1]
        connections_matrix[v][w] = connections_matrix[w][v] = 1


def detect_dead_ends(c):
    for i in range(1, locations + 1):
        for j in range(1, locations + 1):
            if connections_matrix[i][j] == 1:
                if is_dead_end(i, [], [i, j]):
                    global total_dead_ends
                    total_dead_ends += 1
                    dead_ends_list.append([i, j])


def is_dead_end(v, traversed, l):
    x = l[0]
    y = l[1]
    s = 0
    for i in range(1, locations + 1):
        s = s + connections_matrix[y][i]
    if s == 1:
        return True
    else:
        d = True
        for i in range(1, locations + 1):
            if connections_matrix[y][i] == 1 and i != x:
                if i == v:
                    d = False
                    break
                elif [y, i] not in traversed:
                    traversed.append([y, i])
                    d = is_dead_end(v, traversed, [y, i])
                    if not d:
                        break
        return d


def remove_unwanted_dead_ends(d):
    global total_dead_ends
    for i in d:
        for j in d:
            if i[1] == j[0] and j[1] != i[0]:
                d.remove(j)
                total_dead_ends -= 1
            elif i[0] == j[1] and i[1] != j[0]:
                d.remove(i)
                total_dead_ends -= 1


def input_command_line():
    global locations, streets, streetsList
    locations = int(sys.argv[1])
    streets = int(sys.argv[2])
    j = 3
    for i in range((len(sys.argv) // 2) - 1):
        if j == len(sys.argv):
            break
        else:
            streetsList.append([int(sys.argv[j]), int(sys.argv[j + 1])])
            j += 2

    connections(locations, streetsList)
    detect_dead_ends(connections_matrix)
    remove_unwanted_dead_ends(dead_ends_list)
    print(total_dead_ends)
    for i in dead_ends_list:
        print(i[0], end=' ')
        print(i[1])


input_command_line()
