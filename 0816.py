# 더 맵게(Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# 섞은 음식의 스코빌 지수 : 스코빌 최소 + (스코빌 최소 2번째 * 2)
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 최소힙 형태로 만들어줌

    print(scoville)
    print(scoville[0], scoville[1])
    while True:
        if scoville[0] >= K:
            break
        
        if not scoville[0] or not scoville[1]:
            break
        mixed = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, mixed)
        answer += 1
    return answer

print(solution([1,2,3,9,10,12],7))
