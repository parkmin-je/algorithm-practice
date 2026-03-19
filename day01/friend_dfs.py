fr_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John':   ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike':   ['Summer', 'Justin'],
    'May':    ['Justin', 'Kim'],
    'Kim':    ['May'],
    'Tom':    ['Jerry'],
    'Jerry':  ['Tom'],
}

def dfs_friends(g, start):
    done = set()
    order = []

    def _dfs(p):
        done.add(p)
        order.append(p)
        for x in g[p]:
            if x not in done:
                _dfs(x)

    _dfs(start)
    return order

print("=== DFS: Summer의 모든 친구 ===")
result = dfs_friends(fr_info, 'Summer')
print(result)

print()

print("=== DFS: Jerry의 모든 친구 ===")
result = dfs_friends(fr_info, 'Jerry')
print(result)

def bfs_friends(g, start):
    qu = []
    done = set()
    qu.append(start)
    done.add(start)
    order = []

    while qu:
        p = qu.pop(0)
        order.append(p)
        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)
    return order

print("=== 비교: Summer에서 시작 ===")
print("BFS:", bfs_friends(fr_info, 'Summer'))
print("DFS:", dfs_friends(fr_info, 'Summer'))