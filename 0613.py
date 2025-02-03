import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    times = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    # times = [7,3,9]
    # 한번에 여러개가 쌓이는 경우 : 앞>=뒤 기다린 경우가 됨.
    # 바로 처리되는 경우 : 앞 < 뒤
    index, cnt = 1, 1
    check = False
    prev = times[0] # 처음에는 7, 
    q = deque([times[index]])

    print(f'start : {q}')
    
    while q:
        print(f'index : {index}')
        curr = q.popleft()
        print(f'previous : {prev}, current : {curr}')
        
        if curr <= prev:
            check = True
            print('prev >= curr')
            cnt += 1
        # 바로 처리
        else:
            check = False
            print('prev < curr')
            answer.append(cnt)
            cnt = 1

        prev = curr
        index += 1
        if index >= len(times):
            print(f'lefs check : {check}')
            answer.append(cnt)
        else:
            q.append(times[index])
        print(f'iteration terminated => index : {index}, cnt : {cnt}, q : {q}, answer : {answer} \n')
    
    return answer

print(solution([93,30,55],[1,30,5]))
#print(solution([95,90,99,99,80,99], [1,1,1,1,1,1]))