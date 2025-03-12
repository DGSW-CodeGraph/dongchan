from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_dict = {want[i]: number[i] for i in range(len(want))} 
    
    for i in range(len(discount) - 9): 
        window = discount[i:i+10]  
        window_count = Counter(window)  
        
        if all(window_count[item] >= want_dict[item] for item in want_dict):
            answer += 1  
    
    return answer
