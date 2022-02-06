answer = 0
dartResult = "1D2S#10S"
pt = []
for i, ch in enumerate(dartResult):
    if ch.isdigit():
        if ch == "0" and dartResult[i-1] == "1":
            pt[-1] *= 10
        else:
            pt.append(int(ch))
    else:
        if ch == "D":
            pt[-1] **= 2
        if ch == "T":
            pt[-1] **= 3
        
        if ch == "*":
            if len(pt) == 1:
                pt[-1] *= 2
            else:
                pt[-2] *= 2
                pt[-1] *= 2
        
        if ch == "#":
            pt[-1] *= -1

print(sum(pt))