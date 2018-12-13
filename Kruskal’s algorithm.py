def find(C, u):
    while C[u] != u:
        u = C[u]                 
    return u


def union(C, u, v):
    u = find(C, u)
    v = find(C, v)
    C[u] = v

def kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C = {u:u for u in G}
    for _, u, v in sorted(E):
        if find(C, u) != find(C, v):
            T.add((u, v))
            union(u, v)
    return T
