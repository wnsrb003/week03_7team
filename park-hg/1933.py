import sys
import heapq
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

buildings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
x_list = []
for x, _, y in buildings:
    x_list.extend([x, y])
x_list = list(set(x_list))
x_list.sort()
buildings.sort()


heap = []
for i in range(len(x_list)):
    for x, y, h in buildings:
        if x <= x_list[i]:
            heapq.heappush(heap, (-h, y))
        else:
            break

    cur_h = 0
    while heap and heap[0][1] <= x_list[i]:
        heapq.heappop(heap)
    
    if heap:
        if cur_h != -heap[0][0]:
            cur_h = -heap[0][0]
            print(x, cur_h)

