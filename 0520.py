def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    # h-index : citations 에서 h 이상의 값이 h 개 이상 있는 최댓값
    
    while True:
        l = [ct for ct in citations if ct >= answer]
        if len(l) < answer:
            break
        answer += 1
    
    return answer

print(solution([3,0,6,1,5]))