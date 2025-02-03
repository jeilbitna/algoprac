# https://school.programmers.co.kr/learn/courses/30/lessons/340212
# 이진 탐색 해야할듯 ?
def solution(diffs, times, limit):
    # diff > level 이면 diff - level 만큼 틀림.
    low, high = 0, max(diffs)
    answer = high

    print(f'start low : {low}, high : {high}')
    # limit 보다 많아지는 시점에 종료하면 될듯
    while low <= high:
        mid = (low + high) // 2
        total = 0
        # 알고리즘
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                total += times[i]
            else:
                num = diffs[i] - mid
                total += num * (times[i-1] + times[i]) + times[i]

            if total > limit:
                break

        if total > limit:
            low = mid + 1
        else:
            answer = mid
            high = mid - 1
        print(f'low : {low}, high : {high}')

    if answer < 1:
        return 1
    return answer

print(solution([1,5,3], [2,4,7], 30))

print(solution([1,4,4,2], [6,3,8,2], 59))

print(solution([1,328,467,209,54], [2,7,1,4,3], 1723))

print(solution([1,99999,100000,99995], [9999,9001,9999,9001], 3456789012))


print(solution([1,1], [1,2], 100))

print(solution([1],[1],1))