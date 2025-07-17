def solution(players, callings):
    rank = {}
    for i in range(len(players)):
        rank[players[i]] = i       

    for name in callings:
        # 카이의 인덱스를 찾으면은
        idx = rank[name]
        pre_name = players[idx-1]
        players[idx], players[idx-1] = players[idx-1], players[idx]
        rank[name] -= 1
        rank[pre_name] += 1
    return players