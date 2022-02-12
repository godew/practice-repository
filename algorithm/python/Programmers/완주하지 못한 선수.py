import collections

def solution(participant, completion):
    answer = ''
    participant = collections.Counter(participant)
    for h in completion:
        participant[h] -= 1
    
    participant += collections.Counter()
    return list(participant.elements())[0]