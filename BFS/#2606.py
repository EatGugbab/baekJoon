# No. 2606
# 바이러스
# https://www.acmicpc.net/problem/2606

# -문제
# 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자.
# 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어
# 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다.
# 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.
#
#       1 ㅡㅡ 2 ㅡㅡ 3    4
#        \   /          /
#          5 ㅡㅡ 6    7
#             <그림 1>
#
# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다.
# 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

# -입력
# 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
# 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

# -출력
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

# example input
#
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

from collections import deque


def bfs(v):
    queue = deque()
    queue.append(v)

    # 큐가 있는동안 반복
    while queue:
        v = queue.popleft()
        if v not in ans:
            ans.append(v)
            for i in data:
                a = i[0]
                b = i[1]
                if a == v:
                    queue.append(b)
                elif b == v:
                    queue.append(a)

    return len(ans) - 1


n = int(input())
m = int(input())

data = []
for _ in range(m):
    data.append(list(map(int, input().split())))

# 양방향 간선이기에 노드가 작은 값을 앞으로 정렬
for i in data:
    if i[0] > i[1]:
        i.reverse()
data.sort()

ans = []

print(bfs(1))
