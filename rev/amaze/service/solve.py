def isCell(num):
    return (num & 0x8460800457200004 == 0x8460800457200004)
data = eval(open('kek', 'r').read())

for i in range(0, len(data)):
    for j in range(0, len(data[i])):
        data[i][j] = 0 if not isCell(data[i][j]) else 1

def bfs(graph_to_search, start, end):
    queue = [[start]]
    visited = set()

    while queue:
        # Gets the first path in the queue
        path = queue.pop(0)

        # Gets the last node in the path
        vertex = path[-1]

        # Checks if we got to the end
        if vertex == end:
            return path
        # We check if the current node is already in the visited nodes set in order not to recheck it
        elif vertex not in visited:
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for current_neighbour in graph_to_search.get(vertex, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)

            # Mark the vertex as visited
            visited.add(vertex)

print(data[100][64])

graph = {}

queue = [[0, 1]]
while queue:
    y, x = queue[0]
    n = []
    if y != 0:
        if data[y-1][x] == 1:
            n.append((y-1, x))
            if (y-1, x) not in graph and [y-1, x] not in queue:
                queue.append([y-1, x])
    if x != 0:
        if data[y][x-1] == 1:
            n.append((y, x-1))
            if (y, x-1) not in graph and [y, x-1] not in queue:
                queue.append([y, x-1])
    if y != len(data)-1:
        if data[y+1][x] == 1:
            n.append((y+1, x))
            if (y+1, x) not in graph and [y+1, x] not in queue:
                queue.append([y+1, x])
    if x != len(data)-1:
        if data[y][x+1] == 1:
            n.append((y, x+1))
            if (y, x+1) not in graph and [y, x+1] not in queue:
                queue.append([y, x+1])
    graph[(y, x)]=n
    
    del queue[0]





# Driver Code
res = bfs(graph, (0, 1), (199, 198))
print(res)




curr = res[0]
for i in range(1, len(res)):
    #print(str(curr) + " --->>> " +str(res[i]))
    if curr[0] != res[i][0]:
        print('d' if res[i][0] > curr[0] else 'u', end='')
    if curr[1] != res[i][1]:
        print('r' if res[i][1] > curr[1] else 'l', end='')
    curr = res[i]

#print(graph)
