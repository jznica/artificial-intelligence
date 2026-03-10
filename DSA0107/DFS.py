graph={'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]}

visited=set()

def dfs(node):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for n in graph[node]:
            dfs(n)

dfs('A')