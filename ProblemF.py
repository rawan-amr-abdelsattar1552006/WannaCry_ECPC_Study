t = int(input())

for i in range(t):
    num_of_Q = int(input())
    mushrooms = []
    
    for i in range(num_of_Q):
        Q,x,y = [int(z) for z in input().split(" ")]

        if Q == 1:
            mushrooms.append((x,y))

        elif Q == 2:
            mushrooms.remove((x,y))

        else:
            if len(mushrooms) == 0:
                print(-1)
            else:
                distances = []

                for i in mushrooms:
                    dist = abs(i[0] - x) + abs(i[1] - y)
                    distances.append(dist)
                    
                print(max(distances))
        
        

