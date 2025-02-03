# 코딩테스트 연습 > 완전탐색 > 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations

def solution(k, dungeons):
    answer = 0

    # cur_dungeon : 하나 하나의 던전
    for cur_dungeon in permutations(dungeons):
        cur_k, count = k, 0
        for need, use in cur_dungeon:
            if cur_k >= need:
                count += 1
                cur_k -= use
        
        answer = max(answer, count)
    return answer


