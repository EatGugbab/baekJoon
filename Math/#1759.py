# No. 1759
# 암호 만들기
# https://www.acmicpc.net/problem/1759

# -문제
# 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며
# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다.
# 또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아
# 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다.
# 즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.
#
# 새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다.
# 이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다.
# C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.

# -입력
# 첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15)
# 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다.
# 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.

# -출력
# 각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.

# example input
#
# 4 6
# a t c i s w

l, c = map(int, input().split())

data = list(input().split())

data.sort()
ans = []


def dfs(k, index):
    if len(k) < l:
        for i in range(index, c):
            nk = k.copy()
            nk.append(data[i])
            dfs(nk, i + 1)
    elif len(k) == l:
        count = l
        for i in k:
            if i in ['a', 'e', 'i', 'o', 'u']:
                count -= 1
        if 2 <= count < l:
            ans.append(k)


k = []
dfs(k, 0)

for i in ans:
    for j in i:
        print(j, end='')
    print()
