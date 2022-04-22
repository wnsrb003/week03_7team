import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))

max_ans = -10**9-1
min_ans = 10**9+1
def dfs(result, i):
    global max_ans, min_ans
    if i == N-1:
        max_ans = max(max_ans, result)
        min_ans = min(min_ans, result)
        return

    if op[0]:
        op[0] -= 1
        dfs(result+A[i+1], i+1)
        op[0] += 1
    
    if op[1]:
        op[1] -= 1
        dfs(result-A[i+1], i+1)
        op[1] += 1

    if op[2]:
        op[2] -= 1
        dfs(result*A[i+1], i+1)
        op[2] += 1

    if op[3]:
        op[3] -= 1
        if result < 0:
            dfs(-((-result)//A[i+1]), i+1)
        else:
            dfs(result//A[i+1], i+1)
        op[3] += 1

dfs(A[0], 0)

print(max_ans)
print(min_ans)