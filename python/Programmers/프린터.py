import collections
def solution(priorities, location):
    priorities = collections.deque(priorities)
    res = 0
    while True:
        if priorities[0] != max(priorities):
            priorities.append(priorities.popleft())
            location = (location - 1) % len(priorities)
        else:
            if location == 0:
                return res + 1
            priorities.popleft()
            location -= 1
            res += 1


print(solution([1, 1, 9, 1, 1, 1], 0))