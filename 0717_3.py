from itertools import permutations

def solution(word):
    alphabets = ["A","E","I","O","U"]
    dic = []
    for i in range(1,6):
        permutation = list(permutations(alphabets, i))
        for per in permutation:
            w = ''
            for p in per:
                w += p
            dic.append(w)
    
    dic.sort()
    print(dic)
    return dic.index(word)+1
print(solution("AAAAE"))