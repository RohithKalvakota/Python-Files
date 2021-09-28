'''

Q1).

req = int(input("req:"))
unit = int(input("unit:"))
n = int(input("n:"))
arr = list(map(int,input("arr:").strip().split()))[:n]
total = req * unit

ans = 0
sum = 0
index = 0
for i in arr:
    if sum<total:
        sum+=i
        if sum>=total:
            index = arr.index(i)
print(index+1)

Q2).
    
evenarr = []
oddarr = []
n = int(input())
arr = list(map(int,input().strip().split()))[:n]

for i in range(0,n):
    if i%2 == 0:
        evenarr.append(arr[i])
    else:
        oddarr.append(arr[i])

print(sorted(evenarr))
print(sorted(oddarr))

Q3).
    
arr = list(map(int,input().strip().split()))
maxi = 0 
index = 0

for i in arr:
    if maxi<i:
        maxi = i
        index = arr.index(i)
        

print(maxi)
print(index)

Q4).
    
n = int(input())
a = list(map(int,input().strip().split()))[:n]
even = []
odd = []

for i in range(0,n):
    if a[i]%2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])

nums = even + odd

print(*nums)

keyword = {"break", "case", "continue", "default", "defer", "else", "for", 
"func", "goto", "if", "map", "range", "return", "struct", "type", "var"}

word = input()
if word in keyword:
    print(True)
else:
    print(False)

Q).

n = int(input())
nums = list(map(int,input().strip().split()))[:n]
numlist = []
zero_count = 0
zerolist = []
result = []

for i in range(0,len(nums)):
    if nums[i] != 0:
        numlist.append(nums[i])
    else:
        zerolist.append(nums[i])

print(*(numlist + zerolist))

Q).

string = input()
new_string = ""

for i in string:
    if i.isupper():
        new_string = new_string + i.lower()
    else:
        new_string = new_string + i.upper()
    
print(new_string)

Method 2).

string = input()
print(string.swapcase())

Q).
    
n = int(input())
a = list(map(int,input().strip().split()))[:n]
temp = 0

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
    
print(*a)

Q).

n = int(input())
a = list(map(int,input().strip().split()))[:n]
maxi = a[0]
mini = a[0]

for i in range(0,len(a)):
    if a[i] > maxi:
        maxi = a[i]
    elif a[i] < mini:
        mini = a[i]
    
print(maxi,mini) 

Q).

n = int(input())
a = list(map(int,input().strip().split()))[:n]
target = int(input())
count = 0

for i in range(0,len(a)):
    if target == a[i]:
        count +=1
    else:
        pass

print(count)

Q).

def fact(n):
    facto = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1,n+1):
            facto = facto * i
        return facto
            
n = int(input())
x = fact(n)
print(x)

Q).
    
string = input()

new_string = ""
vowels = {"a","e","o","i","u"}
for i in string:
    if i in vowels:
        new_string+="*"
    else:
        new_string+=i

print(new_string)

Q).
    
n = int(input())
m = int(input())

divisum = 0
nondivisum = 0

for i in range(1,m+1):
    if i%n == 0:
        divisum += i
    else:
        nondivisum += i

print(abs(nondivisum - divisum))

Q).
    
n = int(input())
sum1 = 0

for i in range(1,11):
    print(n*i,end="  ")
    sum1 += (n*i)

print("\n")
print(sum1)
   
Q). 

upper = int(input())
lower = int(input())
rev = 0

for i in range(upper,lower):
    temp = i
    while temp != 0:
        rev = (rev *10) + (temp%10)
        temp = temp/10
        if i == rev:
            print(rev,end=" ")

Q).

num = input()

if int(num)%7 == 0:
    print(1)
else:
    print(0)

Q).
    
string  = input()
hyph = ""
new_string = ""
result = ""

for i in string:
    if i=="-":
        hyph += i
    else:
        new_string += i

result = hyph + new_string
print(result)

Q).

string = input()
ch1 = input()
ch2 = input()

string1 = ""

for i in string:
    if i.lower() == ch1:
        string1 += ch2
    elif i.lower() == ch2:
        string1 += ch1
    else:
        string1 += i

print(string1)

Q).

m,n = map(int,input().split())
summ = 0

for i in range(m,n+1):
    if i%3 == 0 and i%5 == 0:
        summ+=i
    else:
        pass

print(summ)

Q).
    
n = int(input())
a = list(map(int,input().strip().split()))[:n]

even = []
odd = []

for i in range(0,len(a)):
    if i%2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])
    
for i in range(0,len(even)):
    for j in range(i+1,len(even)):
        if even[j]<even[i]:
            even[i],even[j] = even[j],even[i]
        else:
            pass

for i in range(0,len(odd)):
    for j in range(i+1,len(odd)):
        if odd[j]<odd[i]:
            odd[i],odd[j] = odd[j],odd[i]
        else:
            pass
        
print(*even)
print(*odd)

Q).

def stringrotate(stringinput):
    newstring = []
    new = ""
    if len(stringinput)<2:
        return stringinput
    else:
        for i in stringinput:
            newstring.append(i)
        
    t = newstring[0]
    newstring[0] = newstring[-1]
    newstring[-1] = t

    for i in range(0,len(newstring)):
        new+=newstring[i]
    return new

string = input()
print(stringrotate(string))

Q).
    
n = int(input())
a = list(map(int,input().strip().split()))[:n]
d = int(input())

temp = a[:d]
arr = a[d:]
print(*(arr+temp))

Q)

a = list(map(int,input().strip().split()))
b = list(map(int,input().strip().split()))

a = (sorted(a))
b = (sorted(b))

a = list(set(a))
b = list(set(b))

length = len(c)
mid = length-1

if len(c) % 2 != 0:
    print(c[mid])
else:
    print((c[mid]+c[mid+1])/2)
    
Q).

n = int(input())
add = 0
temp = n 

while n> 0:
    r = n%10
    add = add + (r*r*r)
    n //= 10

if temp == add:
    print("Yes")
else:
    print("No")

Q).

start = int(input("Enter the starting number of the range"))
end = int(input("Enter the ending number of the range"))
 
for n in range(start, end+1):
    sum = 0
 
    for i in range(1, n):
        if n%i == 0:
            sum += i
 
    if n == sum:
        print(n)

Q).
    
start = int(input("Enter the starting number of the range"))
end = int(input("Enter the ending number of the range"))
 
count = 0
for i in range(start,end+1):
    for n in range(2,i):
        if i%2 == 0:
            count +=1
    if count == 2:
        print(i)

Q).

n = input()
print(int(n,8))

Q).

n = int(input())
a = list(map(int,input().strip().split()))[:n]
nums = []
zeros = []
for i in range(0,len(a)):
    if a[i] == 0:
        zeros.append(a[i])
    else:
        nums.append(a[i])

result = nums+zeros
print(result)

Q).
    
a = "AEIOUaeiou"

string = input()
new_string = ""

for i in string:
    if i in a:
        pass
    else:
        new_string += i
        
print(new_string)
    
Q).
    
from collections import Counter

n = int(input())

for i in range(n):
    i = list(map(int,input().strip().split()))[:2]
    i = i + i
    
c = Counter(i)    
    
new = c.most_common(1)
print(sorted(new))
    
*************CAPGEMINI***********
q).
    
s = input()
count = 0

for i in range(0,len(s)):
    if s[i] == "#":
        count+=1
    else:
        pass

x = s.replace("#","")
hashes = "#"*count

result = hashes+x
print(result)

Q).

arr = list(map(int,input().strip().split()))
dup = []

for i in arr:
    if i not in dup:
        dup.append(i)
        print("{} occurs {} times".format(i,arr.count(i)))

Q).

a = int(input())
b = int(input())
c = int(input())
print((a**3)+((a**2)*b)+(2*(a**2)*b)+(a*(b**2))+(2*(b**2)*a)+(b**3))

Q).

arr = list(map(int,input().strip().split(",")))

arr = list(set(arr))

mini = arr[0]
maxi = arr[0]

for i in range(0,len(arr)):
    if arr[i]>maxi:
        maxi = arr[i]
    elif arr[i]<mini:
        mini = arr[i]
    else:
        pass
    
arr.remove(maxi)
arr.remove(mini)   
    
    
print(arr[0],arr[-1],sep=",")

Q).


s1 = ['a','b','c','d']
s2 = ['x','y','z']
s3 = ['a','x','b','y','c','z','d']

s1 = s1+s2
s2 = []

for i in s3:
    if i not in s2:
        s2.append(i)

for i in range(0,len(s2)):
    for j in range(i,len(s2)):
        if s2[i]>s2[j]:
            temp = s2[i]
            s2[i] = s2[j]
            s2[j] = temp
        
if s2 == s1:
    print("true")
else:
    print("false")

Q).
 
arr = [[0 for i in range(2)] for i in range(5)]
arr[0][0],arr[0][1] = 11,20
arr[1][0],arr[1][1] = 30,40
arr[2][0],arr[2][1] = 5,10
arr[3][0],arr[3][1] = 40,30
arr[4][0],arr[4][1] = 10,5

hashmap = dict()
for i in range(5):
    firstele = arr[i][0]
    secele = arr[i][1]
    if (secele in hashmap.keys() and hashmap[secele] == firstele):
        print(f"({secele},{firstele})")
    else: 
        hashmap[firstele] = secele

Q).

s = input()
count = 0

new_string = ""
for i in s:
    if i == "#":
        count+=1
        i = ""
        new_string += i
    else:
        new_string += i
        
print("#"*count+new_string)

Q).

string = input()

start = string[-1]

end = string[0]

result = start + string[1:-1] + end

print(result)

Q).

def swap(string):
    start = string[-1]
    end = string[0]
    result = start + string[1:-1] + end
    return result

string = input()
x = []
words = string.split(" ")
result = []

for i in words:
    x.append(swap(i))

print(*x,sep = " ")

Q).
    
def garage(cars,bikes):
    return (cars*4)+(bikes*2)

x = []
n = int(input())

for i in range(n):
    car,bike = input().split(" ")
    x.append(garage(int(car),int(bike)))

print(*x,sep="\n")

Q).
    
nums = [1,1,2]
count = 0
new = []

for i in nums:
    if i not in new:
        new.append(i)

print(new)
        
Q).

nums = [2,7,11,15,2]
count=0

for i in nums:
    count+=1

target = 9
result = []

for i in range(0,count):
    for j in range(i,count):
        if nums[j] + nums[i] == target:
            result.append(i)
            result.append(j)

print(result)

Q).

start = int(input())
end = int(input())

for i in range(start,end+1):
    sum1 = 0
    for n in range(start,i):
        if i%n == 0:
            sum1 +=n
    if i == sum1:
        print(sum1)
            
Q).

n = int(input()) 

arr = list(map(int,input().split()))[:n] 

d = int(input())

print(*(arr[d:]+arr[:d]))    
    
Q).

string = input()
dup = []
new=""

for i in string:
    if i not in dup:
        dup.append(i)
        new += i+str(string.count(i))

print(new)

Q).
    
def spiralOrder(arr):
    ans=[]
    while arr:
        ans+=arr.pop(0)
        arr= (list(zip(*arr)))[::-1]
    return ans
arr=[]
n,m=map(int,input().split())
for i in range(n):
    arr.append(list(map(int,input().split())))
print(*spiralOrder(arr))

Q).

def garage(cars,bikes):
    return (cars*4)+(bikes*2)

x = []
n = int(input())

for i in range(n):
    car,bike = map(int,input().split())
    x.append(garage(car,bike))

print(*x,sep="\n")

Q).
    
start = int(input())
end = int(input())

for i in range(start,end+1):
    for n in range(2,i):
        if i%n == 0:
            break
    else:
        print(i)

Q).

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split())) 

dup1 = []
dup2 = []

for i in arr1:
    if i not in dup1:
        dup1.append(i)

for i in arr2:
    if i not in dup2:
        dup2.append(i)

result = dup1+dup2
temp1 = 0

for i in range(0,len(result)):   
    for j in range(i,len(result)):
        if result[i]>result[j]:
            temp1 = result[i]
            result[i] = result[j]
            result[j] = temp1
half = (len(result)//2)

if len(result)%2 == 0:
    print((result[half]+result[half+1])//2)
else:
    print(result[half])

Q).
    
nums = []
result = []

while 1:
    n = int(input())
    if n<0:
        break
    else:
        nums.append(n)

for i in nums:
    if i%5 == 0 and i%11 == 0:
        result.append(-3)
    elif i%5 == 0:
        result.append(-1)
    elif i%11 == 0:
        result.append(-2)
    else: 
        result.append(i)

print(*result,sep="\n")

nums = []
result = []

while 1:
    n = int(input())
    if n<0:
        break
    else:
        nums.append(n)

for i in nums:
    if i%2!=0 and i>50:
        result.append(-3)
    elif i%2 != 0:
        result.append(-1)
    elif i>50:
        result.append(-2)
    else: 
        result.append(i)

print(*result,sep="\n")

Q).

n = int(input())
x = []

for i in range(n):
    nums = int(input())
    x.append(nums)

string = ""

count = 0
for i in range(len(x)):
    if x[i]%2 == 0 and x[i]//10 == 0:
        string+=str(x[i])
        count+=1
    else:
        pass

if count>0:
    print(string)
else:
    print("Invalid")

Q).

n = 5
x = []
for i in range(5):
    nums = int(input())
    x.append(nums)
    
maxi = x[0]
for i in range(0,len(x)):
    if x[i]>maxi:
        maxi = x[i]
    else:
        pass

print(maxi)
    
Q).

n,target = map(int,input().split())
count = 0

while n>0:
    rem = n%10
    if rem == target:
        count+=1
    n = n//10

print(count)

Q).
    
n = int(input())
nums = list(map(int,input().split()))[:n]
x = []
for i in range(0,len(nums)-1):
        x.append(abs(nums[i]-nums[i+1]))

sum1 = 0
for i in x:
    sum1 += i 
    
print(sum1)

Q).

n = int(input())
nums = list(map(int,input().split()))[:n]
even = []
odd = []

for i in nums:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(*(even+odd))
    
Q).

string = input()
count = 0

for i in string:
    if "a"<=i<="z" or "A"<=i<="Z" or "0"<=i<="9":
        pass
    else:
        count+=1

print(count)

Q).

n = int(input())
nums = list(map(int,input().split()))[:n]
count = 0

for i in range(0,len(nums)):
    if (nums[i]**0.5) % 1 == 0:
        count+=1
    else:
        pass
print(count)

Q).

n = int(input())
high = 0

while n>0:
    rem = n % 10
    if rem>high:
        high = rem
    n = n//10

print(high)

Q).
    
char,n = input().split()

n = int(n)

result = ord(char) + n

if result>90 or result>122:
    result = result-26
elif result<65 or result<97:
    result = result+26


print(chr(result))

Q).

n,low,high = map(int,input().split())

nums = list(map(int,input().split()))[:n]
result = []

for i in range(0,len(nums)):
    if low<nums[i] and nums[i]<high:
        result.append(nums[i])
    else:
        pass

print(*result)

Q).

n = int(input())
result = []
count = 0

while n>0:
    rem = n%10
    result.append(rem)
    n=n//10

dup = []
for i in range(0,len(result)):
    if result[i] not in dup:
        dup.append(result[i])

for i in dup:
    if result.count(i)>1:
        count += 1

print(count)

Q).

nums = list(map(int,input().split()))
x = []

for i in nums:
    if i>0 and i not in x:
        x.append(i)
        
for i in range(0,len(x)):
    for j in range(i,len(x)):
        if x[i]>x[j]:
            x[i],x[j] = x[j],x[i]
   
print(x[-1]+x[-2])
            
Q).

n,k = map(int,input().split())

nums = list(map(int,input().split()))[:n]

for i in range(0,len(nums)):
    for j in range(i,len(nums)):
        if nums[i] > nums[j]:
            nums[i],nums[j] = nums[j],nums[i]
            
print(nums[k-1])
            
Q).

n = int(input())
num = int(input())
count = 0

while n>0:
    rem = n%10
    if rem != num:
        count+=1
    n = n//10

print(count)

Q).

n = int(input())

nums = list(map(int,input().split()))[:n]
count = 0

for i in range(0,len(nums)):
    if nums[i]>0:
        count+=1
    else:
        pass

print(count)

'''
    




 

    








    
    
    
        
        




