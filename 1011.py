def solution(video_len, pos, op_start, op_end, commands):
    answer = timecal(pos)
    for command in commands:
        if answer >= timecal(op_start) and answer <= timecal(op_end):
            answer = timecal(op_end)

        if command == 'prev':
            if answer < 10:
                answer = 0
            else:
                answer -= 10
            

        elif command == 'next':
            if timecal(video_len) - answer < 10:
                answer = timecal(video_len)
            else:
                answer += 10
        
        if answer >= timecal(op_start) and answer <= timecal(op_end):
            answer = timecal(op_end)

    return timecal2(answer)

def timecal(time):
    minute, second = map(int, time.split(':'))
    return minute*60 + second

def timecal2(time):
    minute, second = time//60, time%60

    if minute < 10:
        minute = f'0{minute}'
    if second < 10:
        second = f'0{second}'

    return f'{minute}:{second}'




print(solution('34:33', '13:00', '00:55', '02:55', ['next', 'prev']))

print(solution('10:55','00:05','00:15','06:55',['prev','next','next']))

print(solution('07:22', '04:05', '00:15', '04:07', ['next']))