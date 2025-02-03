# https://school.programmers.co.kr/learn/courses/30/lessons/340198

def solution(mats, park):
    # 돗자리는 정사각형 모양임
    mats.sort(reverse=True)
    max_y, max_x = len(park), len(park[0])
    for mat in mats:
        for cy in range(max_y):
            for cx in range(max_x):
                if park[cy][cx] == '-1':
                    if search(max_y, max_x, cy, cx, mat, park) == True:
                        return mat
    return -1

def search(max_y, max_x, cy, cx, mat, park):
    for y in range(mat):
        for x in range(mat):
            if cy + y < 0 or cy + y >= max_y or cx + x < 0 or cx + x >= max_x:
                return False
            if park[cy+y][cx+x] != '-1':
                return False
    return True
