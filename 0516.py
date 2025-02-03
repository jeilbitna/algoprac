import sys

input = sys.stdin.readline

# 숫자 자릿수 별로 다음 수 계산 함수
def calculate(num):
    strnum = str(num)
    lennum = len(strnum)
    sumnum = 0
    for i in range(lennum):
        s = int(strnum[i])
        sumnum += (s**2)

    return sumnum

# 메인 함수
def solution():
    maxnum = int(input()) # 9999

    # 행복수가 담길 리스트
    happynum = []

    for currnum in range(1, maxnum+1):
        memolist = []
        startnum = currnum
        while True:
            # 1은 그냥 행복수
            if startnum == 1:
                happynum.append(startnum)
                break

            nextnum = calculate(currnum)
            # 1 나오면 멈춤
            if nextnum == 1:
                happynum.append(startnum)
                break

            # memolist 에 이미 있으면 순환하는 거    
            if nextnum in memolist:
                break
            else:
                memolist.append(nextnum)
                currnum = nextnum

    #sentence = f"1 ~ {maxnum} 범위의 행복 수는 {len(happynum)}개이고 총합은 {sum(happynum)}입니다."
    return len(happynum) * sum(happynum)


print(solution())