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