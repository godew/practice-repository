import collections
cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
cache = collections.deque()

answer = 0
for city in cities:
    city = city.lower()
    if city in cache:
        answer += 1
        cache.remove(city)
    else:
        answer += 5
    cache.append(city)
    if len(cache) > cacheSize:
        cache.popleft()

print(answer)
