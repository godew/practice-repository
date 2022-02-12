def solution(s):
    my_dict = {"ze" : [0,4],
               "on" : [1,3],
               "tw" : [2,3],
               "th" : [3,5],
               "fo" : [4,4],
               "fi" : [5,4],
               "si" : [6,3],
               "se" : [7,5],
               "ei" : [8,5],
               "ni" : [9,4]}

    res = ""
    i = 0
    while i < len(s):
        if s[i].isdigit():
            res += s[i]
            i += 1
        else:
            res += str(my_dict[s[i] + s[i+1]][0])
            i += my_dict[s[i] + s[i+1]][1]
    return res

print(solution("2three45sixseven"))