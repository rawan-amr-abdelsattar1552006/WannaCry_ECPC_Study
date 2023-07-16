"""
from itertools import combinations


n,m,k = [int(x) for x in input().split(" ")]
nums = [int(x) for x in input().split(" ")]

nums = nums[:m+k]

current_max = 0

new_list = list(combinations(nums, m))
sums = [sum(i) for i in new_list]

print(max(sums))

"""

'''
7 4 2
100 500 250 400 300 150 200
for index_i,i in enumerate(nums):
    
    for index_j,j in enumerate(nums):
    
        if index_j == index_i:
            continue
        if i + j > current_max:
            current_max = i + j
print(current_max)
'''          

n,m,k = [int(x) for x in input().split(" ")]
nums = [int(x) for x in input().split(" ")]

nums = nums[:m+k]

current_max = 0

new_list = sorted(nums, reverse=True)


print(sum(new_list[:m]))
        


