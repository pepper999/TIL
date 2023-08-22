import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    string = [list(input()) for _ in range(5)]
