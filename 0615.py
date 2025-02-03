def solution(s):
    answer = True
    stack = []

    for i in range(len(s)):
        p = s[i]
        print(f'p : {p}')
        if p == '(':
            stack.append(p)
        elif p == ')':
            if not stack:
                print('stack is empty!')
                answer = False
                break
            stack.pop()
        
        print(f'current stack : {stack}')
    
    if stack:
        answer = False
    return True

#print(solution("()()"))
#print(solution("(())()"))
print(solution(")()("))
#print(solution("(()("))