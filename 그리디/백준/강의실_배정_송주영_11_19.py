import sys
import heapq
sys.stdin = open('./그리디/백준/강의실_배정_송주영_11_19.txt')
input = sys.stdin.readline # input() 보다 더 빠른 실행
n = int(input().strip()) 
# n개의 수업 # sys.stdin.readline으로 읽었으므로 strip()을 통해 앞뒤 공백 혹은 개행문자 제거

# class 목록
class_list = [list(map(int, input().split())) for _ in range(n)]
# 시작 시간을 기준으로 오름차순 정렬
class_list.sort(key=lambda x: x[0])
print('class_list\n',class_list, sep ='')

rooms = []

for start, end in class_list:
    if rooms and rooms[0] <= start: # room에 리스트가 성분이 존재한 뒤에 rooms의 첫 요소를 따진다.
        heapq.heappop(rooms)

    heapq.heappush(rooms, end)

    print('rooms', rooms, 'rooms[0]', rooms[0])
    print(rooms)
print(len(rooms))