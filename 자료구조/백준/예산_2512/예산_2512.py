import sys
sys.stdin = open('./자료구조/백준/예산_2512_1.txt')
# sys.stdin = open('./자료구조/백준/예산_2512_2.txt')
input = sys.stdin.readline

# 값 입력
n = int(input())
numbers = list( map( int, input().split() ))
budgets = int(input())

low, high = 0, max(numbers)

# 이진탐색을 통해 원하는 값이 나올 때까지 탐색한다.
# allocation(=배정금액) < budgets(=현재예산)인 경우는 탐색 범위에 답이 존재하므로 하한값 low를 늘려가며, 값을 찾는다.
# allocation(=배정금액) > budgets(=현재예산)인 경우는 탐색 범위에 답이 없으므로 상한값 high을 줄인다.
# 위아래로 값을 계속 제거하다보면 high = low인 순간(=교차 지점)이 존재할 것이다.(=그래프로 생각)
# 교차 지점에서 문제의 조건을 만족한다.
while low <= high:
    mid = (low + high) // 2
    allocation = sum( min(budget, mid) for budget in numbers  )
    
    # 계산을 했을 때, 총 배정액이 총 예산보다 크면, high(=배정 상한액)을 작게 한다.
    # 계산을 했을 때, 총 배정액이 총 예산보다 작다면, low(=배정 상한액)을 작게 한다.
    if allocation > budgets:
        high = mid - 1
    else:
        low = mid + 1

print(high)