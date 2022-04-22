import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

nums = []
while True:
    line = sys.stdin.readline().rstrip()
    if not line:
        break
    nums.append(int(line))

def postorder(nums):
    if nums:
        root = nums[0]
        idx = len(nums)
        for i in range(1, len(nums)):
            if nums[i] > root:
                idx = i
                break
            
        postorder(nums[1:idx])
        postorder(nums[idx:])
        print(root)

postorder(nums)