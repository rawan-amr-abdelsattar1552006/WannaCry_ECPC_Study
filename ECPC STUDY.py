
# Sheet #1 Problem A

"""
# Sheet #1 Problem B

inputs = input().split(" ")
for var in inputs:
    print(var)
"""


"""
# Sheet #1 Problem C

nums = input().split(" ")

x = int(nums[0])
y = int(nums[1])

print(f"{x} + {y} = {x + y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} - {y} = {x - y}")

"""
"""
# Sheet #1 Problem D

a,b,c,d = [int(i) for i in input().split(" ")]

X = (a * b) - (c * d)

print(f"Difference = {X}")
"""

"""
# Sheet #1 Problem E

x = float(input())
pi = 3.141592653

a = pi * x ** 2

print(round(a,9))
"""

"""
# Sheet #1 Problem F

nums = input().split(" ")
print(int(nums[0][-1]) + int(nums[1][-1]))
"""

"""
#Sheet #1 Problem G

n = int(input())

Sum = (n * (n+1)) / 2

print(int(Sum))

"""

"""
# Sheet #1 Problem H

import math

x,y = [int(x) for x in input().split(" ")]

def roundNum(num):
    num = num.split(".")
    x = float(f"0.{num[1]}")
    if float(f"{x:.1f}") >= 0.5:
        num = int(num[0]) + 1
    else:
        num = int(num[0])
    return num

print(f"floor {x} / {y} = {math.floor(x / y)}")
print(f"ceil {x} / {y} = {math.ceil(x / y)}")
print(f"round {x} / {y} = {roundNum(str(x / y))}")

"""

"""
# Sheet #1 Problem I

a,b = [int(x) for x in input().split(" ")]

if a >= b:
    print("Yes")
else:
    print("No")
"""

"""
# Sheet #1 Problem J

a,b = [int(x) for x in input().split(" ")]

if a % b == 0 or b % a == 0:
    print("Multiples")
else:
    print("No Multiples")

"""

"""
# Sheet #1 Problem K

nums = [int(x) for x in input().split(" ")]
print(min(nums),max(nums))

"""

"""
# Sheet #1 Problem L

person1 = input().split(" ")
person2 = input().split(" ")

if person1[1] == person2[1]:
    print("ARE Brothers")
else:
    print("NOT")
"""

"""
# Sheet #1 Problem M

#48-57 digits
#65-90 alpha cap
#97-122 alpha small


ascii_code = ord(input())

if ascii_code >= 48 and ascii_code <= 57:
    print("IS DIGIT")
else:
    print("ALPHA")
    if ascii_code >= 65 and ascii_code <= 90:
        print("IS CAPITAL")

    else:
        print("IS SMALL")

"""
"""
# Sheet #1 Problem N

char = input()

if char.isupper():
    print(char.lower())
else:
    print(char.upper())
"""

"""
# Sheet #1 Problem O

op = input()

if "+" in op:
    a,b = [int(x) for x in op.split("+")]
    print(a + b)
elif "-" in op:
    a,b = [int(x) for x in op.split("-")]
    print(a - b)
elif "*" in op:
    a,b = [int(x) for x in op.split("*")]
    print(a * b)
else:
    a,b = [int(x) for x in op.split("/")]
    print(a//b)
"""

"""
# Sheet #1 Problem P

num = input()

if int(num[0])% 2 == 0:
    print("EVEN")
else:
    print("ODD")
"""

"""
# Sheet #1 Problem Q

x,y = [float(i) for i in input().split(" ")]

if x == 0 and y == 0:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")
elif x > 0 and y > 0:
    print("Q1")
elif x > 0 and y < 0:
    print("Q4")
elif x < 0 and y < 0:
    print("Q3")
elif x < 0 and y > 0:
    print("Q2")
"""

"""
# Sheet #1 Problem R

days = int(input())

years = days // 365
months = (days - years * 365) // 30
day = days - years * 365 - months * 30

print(f"{years} years\n{months} months\n{day} days")

"""

"""
# Sheet #1 Problem S

num = float(input())

if num >= 0 and num <= 25:
    print("Interval [0,25]")
elif num > 25 and num <= 50:
    print("Interval (25,50]")
elif num > 50 and num <= 75:
    print("Interval (50,75]")
elif num > 75 and num <= 100:
    print("Interval (75,100]")
else:
    print("Out of Intervals")

"""

"""
# Sheet #1 Problem T

nums = [int(num) for num in input().split(" ")]

for num in sorted(nums):
    print(num)
    
print()

for num in nums:
    print(num)
    
"""

"""
# Sheet #1 Problem U

num = input().split(".")

if float(f"0.{num[1]}") == 0:
    print(f"int {num[0]}")
else:
    print(f"float {num[0]} 0.{num[1]}")
"""

"""
# Sheet #1 Problem V

comp = input()

if "<" in comp:
    a,b = [int(i) for i in comp.split(" < ")]
    if a < b:
        print("Right")
    else:
        print("Wrong")
        
elif ">" in comp:
    a,b = [int(i) for i in comp.split(" > ")]
    if a > b:
        print("Right")
    else:
        print("Wrong")

elif "=" in comp:
    a,b = [int(i) for i in comp.split(" = ")]
    if a == b:
        print("Right")
    else:
        print("Wrong")

"""

"""
# Sheet #1 Problem W

eq = input().replace(" ","").split("=")
c = int(eq[1])

if "+" in eq[0]:
    a,b= [int(x) for x in eq[0].split("+")]
    if a + b == c:
        print("Yes")

    else:
        print(a + b)

elif "-" in eq[0]:
    a,b = [int(x) for x in eq[0].split("-")]
    if a - b == c:
        print("Yes")

    else:
        print(a - b)

elif "*" in eq[0]:
    a,b = [int(x) for x in eq[0].split("*")]
    if a * b == c:
        print("Yes")

    else:
        print(a * b)

"""

"""
# Sheet #1 Problem X

a1,b1,a2,b2 = [int(x) for x in input().split(" ")]
boundaries = []

if a1 >= a2 and a1 <= b2:
    boundaries.append(a1)
    if b1 >= a2 and b1 <= b2:
        boundaries.append(b1)
    elif b2 >= a1 and b2 <= b1:
        boundaries.append(b2)
    print(f"{boundaries[0]} {boundaries[1]}")
    
elif a2 >= a1 and a2 <= b1:
    boundaries.append(a2)
    if b1 >= a2 and b1 <= b2:
        boundaries.append(b1)
    elif b2 >= a1 and b2 <= b1:
        boundaries.append(b2)
    print(f"{boundaries[0]} {boundaries[1]}")

else:
    print(-1)
"""

"""
#Sheet #1 Problem Y

a,b,c,d = [int(x) for x in input().split(" ")]

product = str(a * b * c * d)

print(product[-2:])
"""

"""
#Sheet #1 Problem Z

a,b,c,d = [int(x) for x in input().split(" ")]

if a == c and b > d and a!=1:
    print("YES")
elif a > c and b >= d:
    print("YES")
elif a==c and b==d:
    print("NO")
elif (a)**(b) > (c)**(d):
    print("YES")
else:
    print("NO")
"""


"""
# ICPC Assiut : Contest#1 Problem A

line = input().split(" ")
print(f"{-int(line[1])/(-1+(int(line[0])/100)):.2f}")

"""


"""
# ICPC Assiut : Contest#1 Problem B

inputs = input().split(" ")

memo = int(inputs[0])
momo = int(inputs[1])

num = int(inputs[2])

if memo % num == 0:
    if momo % num == 0:
        print("Both")
    else:
        print("Memo")
elif momo % num == 0:
    print("Momo")
else:
    print("No One")
    
"""
"""
# ICPC Assiut : Contest#1 Problem C

import string

letter = input()

alphabet = list(string.ascii_lowercase)

if alphabet.index(letter) + 1 >= len(alphabet):
    print(alphabet[0])
else:
    print(alphabet[alphabet.index(letter) + 1])


"""
"""
# ICPC Assiut : Contest#1 Problem D

a,b,c,d = [int(x) for x in input().split(" ")]

if a + b - c == d  or a - b + c == d or a * b + c == d or a * b - c == d or a + b * c == d or a - b * c == d :
    print("YES")

else:
    print("NO")
    
"""

"""
# ICPC Assiut : Contest#1 Problem E

a,b = [int(x) for x in input().split(" ")]

if a == 0 and b == 0:
    print("NO")
    
elif (a - b) in [0,1,-1]:
    print("YES")

else:
    print("NO")
"""

"""
# ICPC Assiut : Contest#1 Problem F

a,b = [int(x) for x in input().split(" ")]
print(a ^ b)

"""




# ICPC Assiut : Contest#1 Problem G

"""
# ICPC Assiut : Contest#1 Problem H

n,k,a = [int(x) for x in input().split(" ")]

result = (n*k) / a

if (n * k) % a != 0:
    print("double")
elif result >= - 2147483648 and result <= 2147483647:
    print("int")
else:
    print("long long")

"""



"""
# ICPC Assiut : Contest#1 Problem I

a,b = [int(x)  for x in list(input())]

if b == 0:
    print("YES")

elif a % b == 0 or b % a == 0:
    print("YES")
        
else:
    print("NO")
"""



