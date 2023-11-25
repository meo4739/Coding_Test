import sys
sys.stdin = open('./그리디/백준/센서_송주영_11_19_1.txt')
# sys.stdin = open('./그리디/백준/센서_송주영_11_19_1.txt')
input = sys.stdin.readline
num_sensor = int(input().strip())
num_center = int(input().strip())
location = list( map( int, input().split() ))
location.sort()
print(location)
minus = []

for i in range(1,len(location)):
    minus.append(location[i] - location[i-1] )

print(minus)

minus.sort(reverse = True)

print(sum(minus[num_center - 1:]))
