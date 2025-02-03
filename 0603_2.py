def solution(n, computers):
    visited = [False for _ in range(n)]
    answer = 0

    for index in range(n):
        if not visited[index]:
            dfs(n, computers, visited, index)
            answer += 1

    return answer

def dfs(n, computers, visited, index):
    visited[index] = True # 방문 기록 처리
    computer = computers[index]
    for new_index in range(n):
        if computer[new_index] == 0:
            continue
        dfs(n, computers, visited, new_index)

print(solution(3,[[1,1,0],[1,1,0],[0,0,1]]))