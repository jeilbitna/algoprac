from collections import deque
import sys
sys.setrecursionlimit(10**6)

def find(word, words, graph):
    # word : hit, hot, dot, dog, lot ,, ....
    for word_comp in words:
        if word == word_comp:
            continue
        cnt = 0
        for i in range(len(word)):
            if word[i] != word_comp[i]:
                cnt += 1
        if cnt == 1:
            graph[word].append(word_comp)
    

def solution(begin, target, words):
    answer = 0
    words.append(begin)
    #print(f"begin : {begin}, target : {target}, words : {words}")
    # target이 존재하지 않는 경우
    if target not in words:
        return answer
    
    graph = dict(zip(words, [[] for _ in range(len(words))])) # 단어들의 연결 상태를 그래프로 나타내기
    visited = dict(zip(words, [False for _ in range(len(words))])) # 방문 기록 나타내기

    # 1. 그래프 채우기
    for word in words:
        find(word, words, graph)
    
    #print(graph)
    
    # # 2. DFS
        
    q = deque([[begin, 0]])

    while q:
        current_node, cnt = q.pop()
        if current_node == target:
            break
        # 방문 처리
        if not visited[current_node]:
            visited[current_node] = True
        
        for next_node in graph[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append([next_node, cnt+1])
    
    answer = cnt

    return answer

print(solution(begin="hit",target="cog",words=["hot","dot","dog","lot","log","cog"]))

print(solution(begin="hit", target="cog", words=["hot", "dot", "dog", "lot", "log"]))