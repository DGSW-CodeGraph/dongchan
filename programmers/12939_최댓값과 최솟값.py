def solution(s):
    answer = ''
    l = []
    s = s.split(' ')
    for i in s:
        l.append(int(i))
    return str(min(l))+ " " + str(max(l))
