from collections import deque

def solution(tickets):
    answer = []
    graph = {}

    tickets.sort()
    for ticket in tickets:
        start, end = ticket[0], ticket[1]
        if start not in graph:
            graph[start] = [[end, False]]
        else:
            graph[start].append([end, False])
    
    print(f'graph : {graph}')
    q = deque(["ICN"])

    # 경로 실패하면 다시 돌아가서 재탐색 해야함. 
    while q:
        current_node = q.popleft()
        print(f'current node : {current_node}')
        answer.append(current_node)
        if current_node in graph:
            for i in range(len(graph[current_node])):
                next_info = graph[current_node][i]
                next_node, visited = next_info[0], next_info[1]
                if next_node not in graph:
                    continue
                if not visited:
                    graph[current_node][i][1] = True
                    q.append(next_node)
                    break

    return answer

#print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
