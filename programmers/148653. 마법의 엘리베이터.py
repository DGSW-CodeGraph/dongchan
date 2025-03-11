def solution(storey):
    answer = 0
    while storey:
        storey, remain = storey//10, storey%10
        if remain < 5 or (remain == 5 and storey%10 < 5) : answer += remain
        else: 
            answer += (10 - remain)
            storey += 1
    return answer
