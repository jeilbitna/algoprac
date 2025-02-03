from itertools import permutations

def isPrimeNumber(n):
    if n <= 1:
        return False
    for i in range(2,n+1):
        if i != n and n%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = list(numbers)
    all_numbers = []
    for i in range(1, len(nums)+1):
        permutation = list(permutations(nums, i))
        for per in permutation:
            num = ''
            for p in per:
                num += p
            all_numbers.append(int(num))
    
    all_numbers = list(set(all_numbers))
    all_numbers = [num for num in all_numbers if isPrimeNumber(num)]

    return len(all_numbers)

print(solution("17"))
print(solution("011"))