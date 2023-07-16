"""
1
9
5 2 2 2 3 3 3 3 7

t = int(input())
no_of_int = int(input())

nums = [int(x) for x in input().split(" ")]
set_of_nums = set(nums)

if len(list(set_of_nums)) == 1:
    print(0)

element_count = {}


for i in set_of_nums:
    element_count[i] = nums.count(i)
    
keys = list(element_count.keys())
values = list(element_count.values())
chosen_value = keys[values.index(max(values))]

count = 0

for num in nums:
    n = num
    if n % 2 == 0  and n < chosen_value :
        n -= 1
        n += (chosen_value - n )
        count += (chosen_value - n + 1)

        print(f"element : {n} count : {count}")
        
    elif n % 2 == 0  and n > chosen_value:
        n -= (n - chosen_value)
        count += (n - chosen_value)
        print(f"element : {n} count : {count}")

    elif n % 2 != 0  and n < chosen_value :
        n += (chosen_value - n )
        count += (chosen_value - n)
        print(f"element : {n} count : {count}")
        
    elif n % 2 != 0  and n > chosen_value:
        n += 1
        n -= (n - chosen_value)
        count += (n - chosen_value + 1)
        print(f"element : {n} count : {count}")
    
    
"""


t = int(input())

for i in range(t):
    no_of_int = int(input())

    nums = [int(x) for x in input().split(" ")]
    set_of_nums = set(nums)

    if len(list(set_of_nums)) == 1:
        print("ALL EQUALS") # CHANGE THIS TO be ZERO

    costs = []

    element_count = {}


    for i in set_of_nums:
        element_count[i] = nums.count(i)
        
    keys = list(element_count.keys())
    values = list(element_count.values())
    chosen_value = keys[values.index(max(values))]



    """for i in set_of_nums:
        #chosen_value = i
        count = 0 
      """
    count = 0
    for num in nums:
        n = num
        if n % 2 == 0  and n < chosen_value :
            n -= 1 
            n += chosen_value - n
            count += chosen_value - n + 1 
            

            print(f"element : {n} count : {count}")
            
        elif n % 2 == 0  and n > chosen_value:
            n -= n - chosen_value
            count += n - chosen_value
            
            
            print(f"element : {n} count : {count}")

        elif n % 2 != 0  and n < chosen_value :
            n += chosen_value - n 
            count += chosen_value - n 
            
            
            print(f"element : {n} count : {count}")
            
        elif n % 2 != 0  and n > chosen_value:
            n += 1 
            n -= n - chosen_value
            count += n - chosen_value + 1 
            
            
            print(f"element : {n} count : {count}")


            
    print(count)
