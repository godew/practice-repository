def solution(table, languages, preference):
    res = [0] * len(table)
    languages_arr = []
    for i in range(len(table)):
        tmp = table[i].split()
        languages_arr.append(tmp[0])
        for j in range(1, len(tmp)):
            for k in range(len(languages)):
                if tmp[j] == languages[k]:
                    res[i] += preference[k] * (6 - j)
                    break
    
    return sorted(list(zip(res, languages_arr)), key= lambda x : (-x[0], x[1]))[0][1]
    


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],["PYTHON", "C++", "SQL"],[7, 5, 5]))