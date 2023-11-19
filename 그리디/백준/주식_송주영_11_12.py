import sys
sys.stdin = open('./그리디/백준/주식.txt')

d = int(input())
for _ in range(d):
    n = int(input()) # 날의 수를 입력받는다.
    prices = list(map(int, input().split() )) 
    print('prices', prices)
    max_profit = 0
    max_price = 0
    
    for price in reversed(prices):
        print('\n반복문 시작')
        print('price', price)
        if price > max_price:
            print('max_pirce 업데이트')
            max_price = price
            print('max_profit', max_profit)
            print('max_price', max_price)
        else:
            print('max_profit 업데이트')
            max_profit += max_price - price
            print('max_profit', max_profit)
            print('max_price', max_price)
    print(max_profit)
