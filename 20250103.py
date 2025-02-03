# 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    # 정렬을 하면 연산 600만번
    phone_book.sort()
    n = len(phone_book)
    for i in range(n-1):
        curr, next = phone_book[i], phone_book[i+1]
        if curr == next[:len(curr)]:
            answer = False
    return answer


# test case
t1 = ["119", "97674223", "1195524421"]
t2 = ["123","456","789"]
t3 = ["12","123","1235","567","88"]

#print(solution())