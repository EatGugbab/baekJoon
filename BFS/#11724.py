# No. 11724
# 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

# -문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# -입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.(1 ≤ u, v ≤ N, u ≠ v)
# 같은 간선은 한 번만 주어진다.

# -출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

# example input
#
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6

from collections import deque


def bfs(v):
    queue = deque()
    queue.append(v)
    visit[v] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visit[i] != True:
                queue.append(i)
                visit[i] = True


n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
# ex) graph : [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
visit = [False] * (n + 1)

for i in range(1, n + 1):
    if visit[i] == True:
        continue
    bfs(i)
    ans += 1

print(ans)
