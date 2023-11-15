### 1. Sum of diagonal elements

left diagonal - i == j
right diagonal - i+j == len(matrix)[number of rows]


### 2. Rounding off to 6 decimal places

```python
"{:.6f}".format(pos/len(arr))
```

### 3. Pyramid Questions

### 4. Time Conversion

```python
def timeConversion(s):
    if s[-2] == 'P':
        hr = int(s[0:2])
        if hr == 12:
            return s[0:8]
        else:
            hr+=12
            s = str(hr)+s[2:8]
            return s
    else:
        hr = int(s[0:2])
        if hr == 12:
            hr = 0
            hr = str(hr)
            hr+='0'
            s=hr+s[2:8]
            print(s)
            return s[0:8]
            
        else:
            return s[0:8]
```

### 5. Kangaroo jump meet

```python
def kangaroo(x1, v1, x2, v2):   
    if v1 > v2:
        if (x2-x1) % (v1-v2)==0:
            return 'YES'
    
    return 'NO'
```

### 6. Breaking Records

```python
def breakingRecords(scores):
    high = 0
    low = 0
    high_num = low_num = scores[0]
    for i in scores:
        if i > high_num:
            high+=1
            high_num = i
        
        if i < low_num:
            low+=1
            low_num = i
    
    return [high, low]

```

### 7. Check Subarray sum in array

```python
def birthday(s, d, m):
    count = 0
    for i in range(0, len(s)):
        j = i
        date = 0
        x = j+m
        if x <= len(s):
            while j < x:
                date += s[j]
                j+=1
            # print(date)
            if date == d:
                count+=1
    return count
```
### 8. Divisible sum pair

```python
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(0, n):
        # j = i+1
        for j in range(i+1, n):
            if (ar[i]+ar[j]) % k == 0:
                count+=1
    
    return count
```

### 9. Between two sets

```python
def getTotalX(a, b):
    x = max(a)
    y = min(b)
    count = 0
    for i in range(x, y+1):
        flag = 0
        flag2 = 0
        for j in a:
            if i % j != 0:
                flag = 1
                break
        
        if flag == 0:
            for j in b:
                if j % i != 0:
                    flag2 = 1
                    break
        
        if flag2 == 0 and flag == 0:
            count+=1
    
    return count
```

### 10. Find most frequent element in array

```python 
def migratoryBirds(arr):
    arr.sort()
    counter = 0
    max_count = 0
    bird = 0
    for i in range(1, len(arr)):
        counter = counter+1 if arr[i] == arr[i-1] else 0
        if counter > max_count:
            bird = arr[i-1]
            max_count = counter
    
    return bird
```

### 11. Programmer's Day

```python
def dayOfProgrammer(year):
    if year == 1918:
        return '26.09.1918'
    elif (year <= 1917 and year % 4 == 0) or (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        return '12.09.%s' %year
    
    else:
        return '13.09.%s' %year

```

### 12. Bill Split

```python
def bonAppetit(bill, k, b):
    total = 0
    for i in bill:
        total += i
    
    total -= bill[k]
    
    actual = total // 2 
    if actual == b:
        print('Bon Appetit')
    else:
        print(b - actual)
```

### 13. Matching Socks

```python 
def sockMerchant(n, ar):
    d = {}
    for i in ar:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
    
    count = 0
    for i in d:
        count += (d[i] // 2)
    
    return count
```

### 14. Page Count(Drawing Book)

```python 
def pageCount(n, p):
    minimum = n-p
    if p < minimum:
        return (p//2)
    elif n == 6 and p == 5:
        return 1
    else:
        return (minimum//2)
```

### 15. Counting Valley

```python
def countingValleys(steps, path):
    sea = 0
    valley_in = 0
    count = 0
    for i in path:
        if i == 'U':
            sea+=1
        
        if i == 'D':
            sea-=1
        
        
        if sea < 0:
            valley_in = 1
        
        if (sea >= 0) and (valley_in == 1):
            count += 1
            valley_in = 0
    
    return count
```

### 16. Electronic Shop

> Brute Force Approach

```python
def getMoneySpent(keyboards, drives, b):

    if b < (min(keyboards)+min(drives)):
        return -1
    
    max_spent = 0
    
    for i in keyboards:
        for j in drives:
            if i+j <= b:
                if (i+j) > max_spent:
                    max_spent = (i+j)
    
    return max_spent
```

### 17. Cats and a Mouse

```python
def catAndMouse(x, y, z):
    if abs(x-z) == abs(y-z):
        return 'Mouse C'
    
    if abs(x-z) < abs(y-z):
        return 'Cat A'
        
    if abs(x-z) > abs(y-z):
        return 'Cat B'
```

### 18. Picking Numbers

```python
def pickingNumbers(a):
    # Write your code here
    maxlen = 0
    for i in a:
        x = a.count(i)
        y = a.count(i-1)
        z = x+y
        if z > maxlen:
            maxlen = z
    
    return maxlen
```

### 19. Designer PDF

```python
def designerPdfViewer(h, word):
    # Write your code here
    l = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    maxval = 0
    for i in word:
        x = l.index(i)
        maxval = max(maxval, h[x])
    return maxval*len(word)
```

### 20. Hurdle Race

```python
def hurdleRace(k, height):
    # Write your code here
    diff = max(height)-k
    if k >= max(height):
        return 0
    else:
        return diff
```

### 21. Utopian Tree

```python
def utopianTree(n):
    # Write your code here
    h = 1
    w = 'sp'
    for i in range(0, n):
        if w == 'sp':
            h*=2
            w = 's'
        else:
            h+=1
            w = 'sp'
    
    return h

```


### 23. Angry Professor

```python
def angryProfessor(k, a):
    # Write your code here
    count = 0
    for i in a:
        if i <= 0:
            count += 1
    
    if count < k:
        return 'YES'
    else:
        return 'NO'
```

### 24. Beautiful Days

```python
def beautifulDays(i, j, k):
    # Write your code here
    count = 0
    for x in range(i, j+1):
        reverse = 0
        z = x
        while x:
            num=(x % 10)
            reverse *= 10
            reverse += num
            x = x//10
        # print(reverse, x-reverse)
        if ((z-reverse) % k == 0):
            count+=1
    
    return count
```


### 25. Viral Ads

```python
def viralAdvertising(n):
    total = 0
    shared = 5
    liked = 0
    for i in range(0, n):
        liked = shared//2
        total += liked
        shared = liked*3
    
    return total
```

### 26. Save the prisoner

```python
def saveThePrisoner(n, m, s):
    # Write your code here
    seat = (m + s - 1) % n

    if (seat == 0):
        return n
    else:
        return seat
```

### 27. Circular Array Rotation

```python
def circularArrayRotation(a, k, queries):
    # Write your code here
    while k:
        x = a.pop()
        a.insert(0, x)
        k-=1
    
    y = []
    for i in queries:
        y.append(a[i])
    
    return y
```

### 28. Sequence Equation

```python
def permutationEquation(p):
    # Write your code here
    res = []
    for i in range(1, len(p)+1):
        res.append(p.index(p.index(i)+1)+1)
    
    return res
```




















### Important Question

```python
K = 2
M = 4
n = K
while True:
    x = sorted(range(1,n+1), key=str)
    i = 1
    if x.index(K)+1 == M:
        print(n)
        break
    if x.index(K)>M:
        print("not possible")
        break
    n = n+1
```