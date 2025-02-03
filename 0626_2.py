from collections import deque

def solution(land):
    answer = 0
    n = len(land) # n = 5 # r
    m = len(land[0]) # m = 8 # c

    dx, dy = [1,-1,0,0], [0,0,1,-1]
    visited = [[False for _ in range(m)] for _ in range(n)] # 전체 방문 처리
    # check_x = [False for _ in range(m)] # x좌표 방문 처리
    counts = [0 for _ in range(m)]
    # land[y][x]

    for x in range(m):
        check_x = [False for _ in range(m)] # x좌표 방문 처리
        for y in range(n):
            cnt = 0
            start = land[y][x]
            if start == 0:
                continue
            # BFS
            if visited[y][x]:
                continue

            q = deque([(x,y)])
            
            while q:
                x, y = q.popleft()
                if visited[y][x]:
                    continue
                #if check_x[x]:
                    #continue
                
                visited[y][x] = True # 전체 방문 처리
                check_x[x] = True # x좌표 방문 처리
                # start = land[y][x]
                
                # if start == 0:
                #     continue

                cnt += 1

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    # 인덱스 예외 처리
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    # 석유 매장 X
                    if land[ny][nx] == 0:
                        continue

                    q.append((nx,ny))
            
            # print(cnt)
            # print(check_x)
            for i in range(len(check_x)):
                check = check_x[i]
                if check:
                    counts[i] += cnt

            print(f'x: {x}, y:{y}, cnt:{cnt}')
    
    
    return max(counts)
print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))

#print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))