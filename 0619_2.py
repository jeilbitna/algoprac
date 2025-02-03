from collections import deque

def solution(prices):
    answer = [i for i in range(len(prices)-1, -1, -1)]
    return answer

print(solution([1,2,3,2,3]))