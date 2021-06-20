# No. 1012
# 유기농 배추
# https://www.acmicpc.net/problem/1012

# -문제
# 한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다.
# 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.
# 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로
# 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.
# 예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다.
# 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.
#
# 1 1 0 0 0 0 0 0 0 0
# 0 1 0 0 1 0 0 0 0 0
# 0 0 0 0 1 0 0 0 0 0
# 0 0 1 1 0 0 0 1 1 1
# 0 0 0 0 1 0 0 1 1 1

# -입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
# 그 다음 줄부터 각각의 테스트 케이스에 대해
# 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50),
# 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다.
# 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다.
# 두 배추의 위치가 같은 경우는 없다.

# -출력
# 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

# example input
#
# 1
# 5 3 6
# 0 2
# 1 2
# 2 2
# 3 2
# 4 2
# 4 0

from collections import deque

# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    # 방문했을 경우 벗어남
    if visited[x][y] == True:
        return False
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        # 벗어난 값 탐색시 벗어남
        if x < 0 or y < 0 or x >= m or y >= n:
            continue
        # 방문했을 경우 벗어남
        if visited[x][y] == True:
            continue

        visited[x][y] = True

        if graph[x][y] == 1:
            # 전방향 탐색
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if [nx, ny] not in queue:
                    queue.append([nx, ny])
    return True


ans = []

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    data = []
    for _ in range(k):
        data.append(list(map(int, input().split())))

    # 그래프 생성 후 값 적용
    graph = [[0 for i in range(n)] for j in range(m)]
    for i in data:
        graph[i[1]][i[0]] = 1

    # 방문 여부
    visited = [[False for i in range(n)] for j in range(m)]

    cnt = 0

    for i in data:
        if bfs(i[1], i[0]) == True:
            cnt += 1

    ans.append(cnt)

for i in ans:
    print(i)
