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

def print_intimacy(g, start):
    qu = []
    done = set()

    qu.append((start, 0))   # (이름, 친밀도) 튜플로 시작
    done.add(start)

    while qu:
        p, d = qu.pop(0)    # 이름이랑 친밀도 같이 꺼내기
        print(p, "친밀도:", d)

        for x in g[p]:
            if x not in done:
                qu.append((x, d + 1))   # 친밀도 1씩 증가
                done.add(x)

print("=== Summer 기준 친밀도 ===")
print_intimacy(fr_info, 'Summer')