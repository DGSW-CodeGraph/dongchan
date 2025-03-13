from collections import deque
def solution(cacheSize, cities):
    if (cacheSize == 0): 
        return 5*len(cities)
    cnt = 0
    cache_storage = deque(maxlen = cacheSize)
    cities = [i.lower() for i in cities]

    for city in cities :
        if city in cache_storage :
            cache_storage.remove(city)
            cache_storage.append(city)
            cnt += 1
        else :
            cache_storage.append(city)
            cnt += 5
    return cnt
