def toposort(graph):
    in_degrees = dict((u,0) for u in graph) 
    for u in graph:
        for v in graph[u]:
            in_degrees[v] += 1  
            start = [u for u in in_degrees if in_degrees[u] == 0]
            result = []
    while start:
        u = start.pop() 
        result.append(u)
        for v in graph[u]:
            in_degrees[v] -= 1 
            if in_degrees[v] == 0: 
                start.append(v) 
    return result
G = {
 'a':'abc',
 'b':'a',
 'c':'c',
 'd':'',
 'e':'f',
 'f':'ec',

}
print(toposort(G))