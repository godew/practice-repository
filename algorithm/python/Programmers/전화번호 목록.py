def solution(phone_book):
    phone_tree = {}
    tmp = phone_tree
    for phone in phone_book:
        for x in phone:
            if -1 in phone_tree:
                return False
            if x not in phone_tree:
                phone_tree[x] = {}
            phone_tree = phone_tree[x]
        else:
            if phone_tree:
                return False
            phone_tree[-1] = None
        
        phone_tree = tmp
    return True


print(solution(["123","456","789", "12"]))

