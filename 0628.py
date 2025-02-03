from collections import deque

dx, dy = [0,-1,0,1], [-1,0,1,0]

def bfs(land, rx, ry):
    q = deque([[rx,ry]])
    n = 1
    visited[rx][ry] = True # 방문 처리
    land[rx][ry] = now

    while q:
        cx, cy = q.popleft() # 현재 위치
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i] # 새로운 위치
            
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == False and land[nx][ny] != 0:
                n += 1
                visited[nx][ny] = True
                land[nx][ny] = now
                q.append([nx,ny])
    oils[now] = n        
    return


def solution(land):
    global r, c, visited, now, oils
    now = 1 # 
    oils = {} # 
    totals = [] # 
    r = len(land) # 세로 길이
    c = len(land[0]) # 가로 길이
    visited = [[False for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            # 석유 매장 안 되어있거나 이미 방문한 경우엔 bfs 안돔
            if land[i][j] == 0 or visited[i][j]:
                continue
            bfs(land, i, j)
            now += 1
