# 의상
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

from collections import defaultdict
def solution(clothes):
    answer = 1
    dic = defaultdict(int)

    for name, kind in clothes:
        dic[kind] += 1
    
    for cnt in dic.values():
        answer *= (cnt+1)

    return answer-1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])

# 개수 : 최소 1개 ~ 최대 dic 의 key 수 개(2개)
# headgear 에서 0~1개 + eyewear 에서 0~1개
# 1개 뽑는건 -> 총 개수
# 2개 뽑는 건 -> 2P1 * 
# solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])