import heapq

graph={
'A':[('B',1),('C',4)],
'B':[('D',2),('E',5)],
'C':[('F',3)],
'D':[],
'E':[],
'F':[]
}

def ucs(start,goal):
    queue=[(0,start)]
    visited=set()

    while queue:
        cost,node=heapq.heappop(queue)

        if node in visited:
            continue

        print(node,"Cost:",cost)

        if node==goal:
            print("Goal Reached")
            return

        visited.add(node)

        for n,c in graph[node]:
            heapq.heappush(queue,(cost+c,n))

ucs('A','F')