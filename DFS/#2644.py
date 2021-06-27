# No. 2644
# 촌수 계산
# https://www.acmicpc.net/problem/2644

# -문제
# 여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

# -입력
# 사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다.
# 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고,
# 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다.
# 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다.
# 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다.
# 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.
#
# 각 사람의 부모는 최대 한 명만 주어진다.

# -출력
# 입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다.
# 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다.
# 이때에는 -1을 출력해야 한다.

# example input
#
# 9
# 7 3
# 7
# 1 2
# 1 3
# 2 7
# 2 8
# 2 9
# 4 5
# 4 6

n = int(input())
x, y = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
result = [0] * (n+1)


def dfs(x):
    for i in graph[x]:
        if result[i] == 0 and i != x:
            result[i] = result[x] + 1
            dfs(i)


dfs(x)

if result[y] == 0:
    print(-1)
else:
    print(result[y])
