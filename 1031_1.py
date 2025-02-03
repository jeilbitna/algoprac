# 코딩테스트 연습 > 완전탐색 > 최소직사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    cur_w, cur_h = sizes[0][0], sizes[0][1]
    answer = cur_w * cur_h

    print(f'start -> cur_w : {cur_w} , cur_h : {cur_h}')
    if len(sizes) == 1:
        return answer
    
    for index, size in enumerate(sizes):
        print(f'index : {index}, w : {size[0]}, h : {size[1]}')
        w, h = size[0], size[1]
        #cur_w, cur_h = max(cur_w, w), max(cur_h, h)
        answer = max(cur_w, w) * max(cur_h, h)

        print(f'w : {w}, h : {h}, cur_w : {cur_w}, cur_h : {cur_h}, answer : {answer}')

        if max(cur_w, h) * max(cur_h, w) < answer:
            print('reversed')
            cur_w, cur_h = max(cur_w, h), max(cur_h, w)
        else:
            cur_w, cur_h = max(cur_w, w), max(cur_h, h)
        
        answer = cur_w * cur_h
        print('\n')
    return answer

#print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))

#print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))

print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))