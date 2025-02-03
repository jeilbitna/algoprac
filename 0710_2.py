def solution(sizes):
    answer = 0
    # 가로 최대, 세로 최대 찾으면 다 넣을 순 있지만 비효율적임 -> 회전 필요함
    # answer = (max_width) * (max_length) 형태
    # max_width : 후보군이 세로 길이 중에도 있음(회전 시)
    # max_length : 후보군이 가로 길이 중에도 있음(회전 시)
    # 가로 최대값 회전시켰을 때와 세로 최대값 회전시켰을 때 경우만 조사하면 될지?
    for w, h in sizes:
        # (60,50), (30,70), (60,30), (80,40)
        # (50,60), (70,30), (30,60), (40,80)
        
    return answer