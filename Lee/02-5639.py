import sys
sys.setrecursionlimit(10**8) # 최대 깊이 설정 안 해주면 런타임 에러뜬다^^

input=sys.stdin.readline

li=[]
while 1:
    try:
        n = int(input())
        li.append(n)
    except:
        break
# 전위 순회(pre)한 결과 list 완성

def post(left,right):
    if left>right:
        return
    mid=right+1 #루트 보다 큰 값이 존재하지 않을 경우 대비
    for i in range(left+1, right+1):
        if li[left] < li[i]: #li[left] == root
            mid=i
            break
        # 값의 처리 및 갱신은 루트노드보다 처음으로 큰 값이 나오는 인덱스가 나올 경우에만
        # 이후는 break로 순회 중단

    post(left+1,mid-1)
    post(mid,right)
    print(li[left])

post(0,len(li)-1)