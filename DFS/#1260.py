# 미해결
# No. 1260
# DFS와 BFS

# -문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# -입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
# 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# -출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
# V부터 방문된 점을 순서대로 출력하면 된다.

# bfs에서 큐 사용을 위해 deque를 import
from collections import deque

n, m, v = map(int, input().split())
data = []
for _ in range(m):
    data.append(list(map(int, input().split())))

# data[i][j]에서 i를 우선으로 정렬, 후 j를 기준으로 정렬됨
data.sort()

# 정답 출력을 위해 초기화
dfsAns = []
bfsAns = []

def small(a,b):
    if a <= b :
        return a, b
    else:
        return b, a


# 방문했는지 체크
visitedD = [False] * m
visitedB = [False] * m


# DFS
def dfs(v):
    if v not in dfsAns:
        dfsAns.append(v)
        for i in range(m):
            a, b = small(data[i][0], data[i][1])
            if a == v and visitedD[i] == False:
                visitedD[i] = True
                dfs(b)
            elif b == v and visitedD[i] == False:
                visitedD[i] = True
                dfs(a)


dfs(v)

# BFS
queue = deque()
queue.append(v)

while queue:
    v = queue.popleft()
    if v not in bfsAns:
        bfsAns.append(v)
    for i in range(m):
        a, b = small(data[i][0], data[i][1])
        if a == v and visitedB[i] == False:
            visitedB[i] = True
            queue.append(b)
        elif b == v and visitedB[i] == False:
            visitedB[i] = True
            queue.append(a)

# DFS, BFS 순으로 정답 출력
for i in dfsAns:
    print(i, end=' ')
print()

for i in bfsAns:
    print(i, end=' ')