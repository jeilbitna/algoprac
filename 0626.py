from collections import deque
#import sys
#sys.setrecursionlimit(10**6)
def bfs(x,y,m,n,land,answers,visited):
    start = land[x][y]
    dx, dy = [0,0,1,-1], [1,-1,0,0] # 동, 서, 남, 북

    q = deque([(x,y)])
    print(f'start => x:{x}, y:{y}')
    cnt = 0
    while q:
        x, y = q.popleft()
        print(f'current => x:{x}, y:{y}, cnt:{cnt}')
        if visited[x][y]:
            continue
        
        visited[x][y] = True

        if land[x][y] == 0:
            continue
        
        cnt += 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or y < 0 or ny >= m:
                print(f'index out of range -> x:{x},y:{y}. continue')
                continue
            q.append((nx,ny))

    answers[x] += cnt

def solution(land):
    # land : 세로 n, 가로 m (mxn)
    # land[i][j] = 1 이어야 석유가 있는 땅
    # 1번열 ~ 6번열까지 차례로 조사
    n = len(land) # n = 5
    m = len(land[0]) # m = 8
    print(f'n:{n}, m:{m}')
    visited = [[False for _ in range(m)] for _ in range(n)]
    answers = [0 for _ in range(m)]
    
    for y in range(n): # 0 <= y < n=5
        for x in range(m): # 0 <= x < m=8
            bfs(x,y,m,n,land,answers,visited)
    
    answer = max(answers)

    return answer

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))