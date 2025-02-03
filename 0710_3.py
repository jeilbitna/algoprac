def solution(bandage, health, attacks):
    answer = 0
    # bandage = [t, x, y] = [시전시간, 초당회복량, 추가회복량]
    # health : 최대체력
    # attacks = [공격 시간, 피해량]
    end_time = attacks[-1][0]
    attacks_time = [t for [t,d] in attacks]

    #print(attacks_time)
    curr_time = 1
    curr_health = health
    curr_cnt = 0
    while curr_time <= end_time:
        # 공격이 있을 때 -> 연속 성공 초기화
        if curr_time in attacks_time:
            curr_cnt = 0
            curr_health -= 
        # 공격이 없을 때
        else:

        
        curr_cnt += 1
        curr_time += 1
    return answer

print(solution([5, 1, 5],30,[[2, 10], [9, 15], [10, 5], [11, 5]]))