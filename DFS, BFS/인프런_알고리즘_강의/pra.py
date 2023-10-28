import sys
sys.stdin = open("input.txt","r") # sys.stdin을 input.txt 파일로 재지정합니다. 따라서 이후에 input() 함수를 사용하면 터미널에서 입력을 받는 대신 input.txt 파일에서 입력을 받게 됩니다.

print(int(input()))
