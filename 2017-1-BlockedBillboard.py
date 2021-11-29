# read from input
import sys
sys.stdin = open("billboard.in", "r")
sys.stdout = open("billboard.out", "w")

class Rect:
    def __init__(self):
        self.x1, self.y1, self.x2, self.y2 = map(int, input().split())

    def area(self):
        return (self.y2 - self.y1) * (self.x2 - self.x1)

def overlap(p, q):
    x_overlap_case1 = min(p.x2, q.x2) - max(p.x1, q.x1)
    x_overlap_case2 = 0
    x_overlap = max(x_overlap_case1, x_overlap_case2)

    y_overlap = max(0, min(p.y2, q.y2) - max(p.y1, q.y1))
    return x_overlap * y_overlap

rects = []
for _ in range(3):
    rects.append(Rect())

total = rects[0].area() + rects[1].area()
overlap = overlap(rects[0], rects[2]) + overlap(rects[1], rects[2])
result = total - overlap
print(result)
