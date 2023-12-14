# Python

## Basics

1. string and tuple is immutable, list, set, dictionary are mutable
2. pip is the package manager for python.
3. match case is the switch statement for python.
4. fstring

```python
name == 'yash'
s = f"my name is {name}"
```

5. try except in python

```python
try:
    num = int(input('Enter number'))
    print(num+4)
except Exception as e:
    print('some error occured', e)
```

6. Context manager for file I/O

```python

s = 'Yash Gupta'
with open('text.txt', 'w') as f:
    f.write(s)

with open('text.txt', 'r') as f:
    x = f.read()

with open('text.txt', 'a') as f:
    f.write('append it')
```
