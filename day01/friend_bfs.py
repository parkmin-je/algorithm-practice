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

print("Summer의 친구:", fr_info['Summer'])
print("May의 친구:", fr_info['May'])

def print_all_friends(g, start):
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        print(p)

        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)

print("=== Summer의 모든 친구 ===")
print_all_friends(fr_info, 'Summer')

print()

print("=== Jerry의 모든 친구 ===")
print_all_friends(fr_info, 'Jerry')