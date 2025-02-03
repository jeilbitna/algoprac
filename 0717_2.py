def solution(brown, yellow):
    answer = []
    total = brown + yellow
    arr = []
    for i in range(1, int(total**0.5)+1):
        # i, total%i
        if total % i == 0:
            arr.append((total//i, i))
    
    print(arr)
    for a in arr:
        x, y = a[0], a[1]
        if (x-2) * (y-2) == yellow:
            return [x,y]
        

print(solution(10,2))