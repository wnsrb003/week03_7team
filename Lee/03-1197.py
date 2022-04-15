import sys

input=sys.stdin.readline

v,e= map(int, input().split())

li=[]
for i in range(e):
    a,b,c=map(int,input().split())
    li.append((c,a,b)) #c,b,a로 넣어야. 가중치로 정점을 두는
    # A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미

# 크루스칼은 정렬이 필요하다.
li.sort(key=lambda x: x[0]) #key 꼭 붙이세용..
parent = list(range(v+1)) #[0, 1, 2, 3]

# union-find
def union(a,b):
    a = find(a)
    b = find(b)

    if b<a:
        parent[a]=b
    else:
        parent[b]=a

def find(a):
    if a== parent[a]:
        return a
    parent[a] = find(parent[a]) #경로를 압축한다
    return parent[a]

sum = 0

for c,a,b in li:
    if find(a) != find(b):
        union(a,b)
        sum+=c

print(sum)
# 이건 디버그 돌려도 어려운데요..? 뭔말이지