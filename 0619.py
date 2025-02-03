from collections import deque

def solution(priorities, location):
    answer = 0
    indexes = [i for i in range(len(priorities))]
    q = deque(list(zip(priorities, indexes)))
    print(q)
    while q:
        priority, index = q.popleft()
        print(f'current ---> priority : {priority}, index : {index}')
        remained = [p[0] for p in q]
        if remained and priority < max(remained):
            q.append((priority, index))
        else:
            answer += 1
            print(f'index : {index} process completed!')
            if index == location:
                break
    return answer

print(solution([1,1,9,1,1,1], 0))
