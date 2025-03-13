def solution(s):
    answer = []
    bin_cnt = 0
    zero_cnt = 0
    while s != '1':
        zero_cnt += s.count('0')
        s = bin(s.count('1'))[2:]
        bin_cnt += 1
    return [bin_cnt, zero_cnt]
