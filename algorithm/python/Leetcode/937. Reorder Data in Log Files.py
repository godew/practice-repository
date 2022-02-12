
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]

letters, digits = [], []
for log in logs:
    if log.split()[1].isdecimal():
        digits.append(log)
    else:
        letters.append(log)

letters.sort(key= lambda x: (x.split()[1:], x.split()[0]))
print(letters+digits)
