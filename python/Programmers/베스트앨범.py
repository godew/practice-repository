import collections
def solution(genres, plays):
    res = []
    genres_dict = collections.defaultdict(list)
    for i, genre in enumerate(genres):
        genres_dict[genre].append([plays[i], i])
    tmp = sorted(genres_dict.items(), key= lambda x : -sum(map(lambda y : y[0], x[1])))

    for genre, plays_list in tmp:
        if len(plays_list) == 1:
            res.append(plays_list[0][1])
            continue
        plays_list.sort(key= lambda x: [-x[0], x[1]])
        res.append(plays_list[0][1])
        res.append(plays_list[1][1])

    return res

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
