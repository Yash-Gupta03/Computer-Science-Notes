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
    # Write your code here
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
    # Write your code here
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
    # Write your code here
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
    # Write your code here
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
    # Write your code here
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
    # Write your code here
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
    # Write your code here
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





























### Important Question

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