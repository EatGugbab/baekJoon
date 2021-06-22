# No. 2908
# 상수
# https://www.acmicpc.net/problem/2908

# -문제
# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다.
# 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다.
# 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.
#
# 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

# -입력
# 첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다.
# 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.

# -출력
# 첫째 줄에 상수의 대답을 출력한다.

# example input
#
# 734 893

# 우선 data에 값을 넣는다.
data = list(map(int, input().split()))

a, b = [], []

# 뒤집기 위해 str로 형변환
for i in str(data[0]):
    a.append(i)

for i in str(data[1]):
    b.append(i)

# 뒤집은 값들이 저장된 리스트를 하나로 묶는다.
a = "".join(reversed(a))
b = "".join(reversed(b))

if a>b:
    print(a)
else:
    print(b)
