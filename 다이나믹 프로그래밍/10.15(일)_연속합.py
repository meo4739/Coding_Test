length = int(input())
seq = list(map( int, input().split() ))

print(f"seq : {seq}")

dp = [0] * length

# dp 세팅 연산을 위해 첫 숫자는 맞춰주고 시작
dp[0] = seq[0]

# 이전 숫자 더해가기
# dp[1] += seq[1] + dp[0]

for i in range(1, len(seq)):     
    dp[i] = max(seq[i], seq[i] + dp[i-1])

print(f"dp :  {dp}")
print(max(dp))

