# read from input
import sys

sys.stdin = open("paint.in", "r")
sys.stdout = open("paint.out", "w")

a, b = map(int, input().split())
c, d = map(int, input().split())

# step 1. calculation
total = (b-a) + (d-c)
intersection = max(min(d, b) - max(a, c), 0)
result = total - intersection
print(result)