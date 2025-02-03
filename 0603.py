from collections import deque

def solution(maps):
    n = len(maps[0]) # 가로 길이
    m = len(maps) # 세로 길이
    visited = [[False for _ in range(n)] for _ in range(m)]
    arrived = []
    dx, dy = [1,-1,0,0], [0,0,1,-1] # 동,서,남,북
    q = deque([(0,0,0)]) # (x좌표, y좌표, 움직인 칸수)
    #visited[0][0] = True

    while q:
        x, y, cnt = q.popleft()

        if visited[y][x]:
            continue

        visited[y][x] = True

        print(f'x : {x}, y : {y}, cnt : {cnt}')
        if y == (m-1) and x == (n-1):
            arrived.append(cnt+1)
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if maps[ny][nx] == 0:
                continue

            q.append((nx, ny, cnt+1))
    
    print(f'arrived : {arrived}')
    answer = min(arrived) if arrived else -1
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))