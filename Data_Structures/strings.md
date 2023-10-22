# Strings in Python

## Basics 
### 1. Either use single quotes or double quotes, for multiline string use triple quotes(single or double) '''yash'''

### 2. Strings are immutable in python.

### 3. Looping in Strings

```python
for x in 'Yash':
    print(x)
```

### 4. Check if string is present

```python
if 'yas' in 'yash':
    print('present')

if 'ya' not in 'yash':
    print('not present')
```

### 5. String Slicing

```python
name = 'Yash Gupta'
print(name[:4])
print(name[0:])
print(name[-1:-6])
```

### 6. String Methods

```python
name = 'Yash Gupta'
print(name.upper())
print(name.lower())
print(len(name))
print(name.strip())
print(name.replace('a','x'))
print(name.split(" "))

list_name = ['Yash', 'Gupta']
new_name = ''.join(list_name)

statement = "My name is {} and my age is {}"
print(statement.format(name[0:4], 24))
```

## Easy Questions

1. Reverse Integer

```python
class Solution:
    def reverse(self, x: int) -> int:
        
        min_int = pow(-2, 31)
        max_int = pow(2, 31)-1
        
        val = str(abs(x))
        val = val[::-1]
        y = int(val)
        
        y = y*(-1) if x < 0 else y
        
        return y if (y < max_int and y >min_int) else 0
```

2. Reverse String

```python
i = 0
j = len(s)-1
while i<j :
    s[i], s[j] = s[j], s[i]
    i+=1
    j-=1
```

3. First Unique Character in a String

```python
def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
                
        for i, val in enumerate(s):
            if d[val] == 1:
                return i
        
        return -1
```

4. Valid Anagram

> We can sort the two strings or find their frequency and return the equated results.

```python
def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # new_s = ''.join(sorted(s))
        # new_t = ''.join(sorted(t))
        
        new_s = (sorted(s))
        new_t = (sorted(t))
        
        for i, val in enumerate(new_s):
            if new_s[i] != new_t[i]:
                return False
        
        return True
```

5. Valid Palindrome
```python
def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        news = ''
        for i in s:
            if i.isalnum():
                news+=i
        
        return news == news[::-1]
```

6. Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
```python
def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) > len(haystack):
            return -1
        
        for i in range(len(haystack)+1-len(needle)):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1
```

7. Longest Common Prefix

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        strs.sort()
        length = min(len(strs[0]), len(strs[-1]))
        i = 0
        while i<length:
            if strs[0][i] == strs[-1][i]:
                res+=strs[0][i]
            else:
                return res
            i+=1
        
        return res
```






