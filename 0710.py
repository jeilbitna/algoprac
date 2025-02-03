def solution(answers):
    result = [[1,0],[2,0],[3,0]]

    p1 = [1,2,3,4,5] # 0,1,2,3,4 // 5,6,7,8,9 // 10 ...
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        answer = answers[i]
        if p1[i%5] == answer:
            result[0][1] += 1
        if p2[i%8] == answer:
            result[1][1] += 1
        if p3[i%10] == answer:
            result[2][1] += 1
    
    result.sort(key=lambda x:x[1], reverse=True)

    r = []
    maxval = result[0][1]
    for p,s in result:
        if maxval == s:
            r.append(p)
    return r

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))