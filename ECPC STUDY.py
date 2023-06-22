# WANNACRY ?! No problem, it's solved !

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


"""

# ICPC Assiut : Contest#1 Problem G

eyes, mouths, bodies = [int(x) for x in input().split(" ")]
looping = True
largest_possible_number = 0

while looping:
    first_method = min([eyes // 2 , bodies])
    second_method = min([eyes // 2 , mouths, bodies])
    third_method = min([eyes, mouths, bodies])

    methods = [first_method, second_method, third_method]
    
    current_max = max(methods)

    print(largest_possible_number, current_max)
    largest_possible_number += current_max
    
    
    index_of_method = methods.index(current_max)

    if current_max == 0:
        looping = False
    
    elif index_of_method == 0:
        eyes -= (current_max * 2)
        bodies -= current_max
        
    elif index_of_method == 1:
        eyes -= (2 * current_max)
        mouths -= current_max
        bodies -= current_max
    else:
        eyes -= current_max
        mouths -= current_max
        bodies -= current_max

    print(eyes, mouths, bodies)
    

print(largest_possible_number)
"""

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

"""
# Sheet #2 Problem A

n = int(input())

for i in range(1,n+1):
    print(i)
"""

"""
# Sheet #2 Problem B
n = int(input())

even = [i for i in range(2, n + 1) if i % 2 == 0]

if even:
    for i in even:
        print(i)
else:
    print(-1)
"""
"""
# Sheet #2 Problem C

num_of_values = int(input())
values = [int(i) for i in input().split()]

even = [i for i in values if i % 2 == 0]
odd = [i for i in values if i % 2 != 0]
positive = [i for i in values if i > 0]
negative = [i for i in values if i < 0]

print(f"Even: {len(even)}")
print(f"Odd: {len(odd)}")
print(f"Positive: {len(positive)}")
print(f"Negative: {len(negative)}")

"""
"""
# Sheet #2 Problem D

trying = True
while trying:
    passwd = input()
    if passwd == "1999":
        print("Correct")
        break
    else:
        print("Wrong")

"""
"""
# Sheet #2 Problem E

num_of_values = int(input())
values = [int(i) for i in input().split(" ")]

max_num = values[0]

for num in values:
    if num > max_num:
        max_num = num
print(max_num)
"""

"""
# Sheet #2 Problem F
n = int(input())

for i in range(1, 13):
    print(f"{n} * {i} = {n * i}")

"""

"""
# Sheet #2 Problem G
num_of_testcases = int(input())

for i in range(num_of_testcases):
    n = int(input())
    factorial = 1

    if n == 0:
        print(1)
    else:
        for j in range(2,n + 1):
            factorial *= j
        print(factorial)

"""
"""
# Sheet #2 Problem H
import math

num = int(input())
sqrt_of_num = int(math.sqrt(num))
isPrime = "YES"
 
if num % 2 == 0 and num != 2:
    isPrime = "NO"
else:
    for i in range(3,sqrt_of_num + 1,2):
        if num % i == 0:
            isPrime = "NO"
print(isPrime)

"""

"""
# Sheet #2 Problem I

num = input()
reverse = num[::-1]

print(int(reverse))

if num == reverse:
    print("YES")
else:
    print("NO")

"""

"""
# Sheet 2 Problem J
import math
num = int(input())
primes = ["2"]

def isPrime(x):
    sqrt_of_num = int(math.sqrt(x))
    isPrime = True
     
    if x % 2 == 0 and x != 2:
        isPrime = False
    else:
        for i in range(3,sqrt_of_num + 1,2):
            if x % i == 0:
                isPrime = False
    return isPrime


for i in range(3,num + 1, 2):
    if isPrime(i):
        primes.append(str(i))

print(" ".join(primes))
"""

"""
# Sheet 2 Problem K

n = int(input())

for i in range(1,n + 1):
    if n % i == 0:
        print(i)
"""

# Sheet 2 Problem L

"""
# Sheet 2 Problem M

a,b = [int(i) for i in input().split(" ")]
lucky = []

def isLucky(x):
    for i in str(x):
        if i not in ["4","7"]:
            return False
       
    return True

for i in range(a,b + 1):
    if isLucky(i):
        lucky.append(str(i))

print(" ".join(lucky) if lucky else "-1")

"""
"""
# Sheet 2 Problem N

symbol = input()
n = int(input())
values = [int(x) for x in input().split(" ")]

for i in range(n):
    print(symbol * values[i])

"""
"""
# Sheet 2 Problem O

symbol = input()
n = int(input())
values = [int(x) for x in input().split(" ")]

for i in range(n):
    print(symbol * values[i])
"""

"""
# Sheet 2 Problem P

n = int(input())

for i in range(n, 0, -1):
    print("*" * i)
"""

"""
# Sheet 2 Problem Q
n = int(input())

for i in range(n):
     num = input()
     reverse = list(num[::-1])
     print(" ".join(reverse))
"""

