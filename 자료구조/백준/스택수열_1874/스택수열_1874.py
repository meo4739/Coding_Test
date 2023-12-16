import sys
sys.stdin = open('./자료구조/백준/스택수열_1874/스택수열_1874.txt')
input = sys.stdin.readline

# 입력값에 대해서는 n과 elements에 할당한다.
n = int(input())
elements =  [int(input()) for i in range(n)]

# 정답과 연산에 필요한 값들은 stack, answer, current에 할당한다.


def stack_sequence(n, elemeents):
    stack, answer = [], []
    current = 1

    for element in elements:
        while current <= element:
            stack.append(current) # 현재 값이 문제에서 입력한 값보다 작다면, 1, 2, 3 스택을 쌓는다.
            answer.append('+')
            current += 1
        if stack[-1] == element: # 쌓인 스택의 마지막 값이 문제에서 입력한 값과 같다면 값을 출력한다.
            stack.pop()
            answer.append('-')
        else:
            return "NO"
    return answer

result = stack_sequence(n, elements)
if result == "NO":
    print("NO")
else:
    for i in result:
        print(i)