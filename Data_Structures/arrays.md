# Arrays in Python

## Definition

Collection of elements stored in contiguous memory location.

`names = ['yash', 'sourabh', 'shivam', 'durgesh']`

## Methods

<details>
<summary> Length of array ?</summary>

`x = len(names)`

</details>

<details>
<summary> Looping in general in python ?</summary>

```python
names = ['yash', 'sourabh', 'shivam', 'durgesh']
for i in names:
    print(i)
```

```python
for i in range(0, 10):
    print(i)
```

```python
for index, value in enumerate(names):
    print(index, value)
```

</details>

<details>
<summary> Add elements in array ?</summary>

```python
names = ['yash', 'sourabh', 'shivam', 'durgesh']
names.append('Rohan') # Adds name at the end

names.insert(1, 'Kshitij') # Adds at any position
```

</details>

<details>
<summary> Delete Elements from array ?</summary>

```python
names.pop(position) # pops from any position

names.remove(element) #removes that element

names.clear() # removes all elements
```

</details>

<details>
<summary> Reverse ?</summary>

```python
names.reverse()
```

</details>

<details>
<summary> All other methods ?</summary>

```python
x = names.count('Yash') # gives freq. of yash

y = names.index('yash') #gives index

new_name = names.copy() # returns a copy

names.sort(reverse=True) # sorts elements
```

</details>

<br>

# Array Easy Practice Questions

1. Remove Duplicates from Sorted Array

> compare elements, increment only when comparison is not equal

```js
var removeDuplicates = function (nums) {
  let i = 1;
  while (i < nums.length) {
    if (nums[i] == nums[i - 1]) {
      nums.splice(i - 1, 1);
    } else {
      i += 1;
    }
  }
  return nums.length;
};
```

2. Best Time to Buy and Sell Stock II

> subtract adjacent value and add to total when i+1 index value is greater than ith value

```js
var maxProfit = function (prices) {
  let i = 1;
  let total = 0;
  while (i < prices.length) {
    if (prices[i] > prices[i - 1]) {
      total += prices[i] - prices[i - 1];
    }
    i++;
  }
  return total;
};
```

3. Rotate Array by k steps towards right

> using reverse technique,
> if reversing towards right then first reverse last k elements, then first n-k, then the whole array.

> if reversing towards left then first reverse first k elements, then last n-k, then the whole array.

```js
var rotate = function (nums, k) {
  let i, j, temp;
  let n = nums.length;
  k = k % n;
  for (i = 0, j = n - k - 1; i < j; i++, j--) {
    temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
  }

  for (i = n - k, j = n - 1; i < j; i++, j--) {
    temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
  }

  for (i = 0, j = n - 1; i < j; i++, j--) {
    temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
  }
};
```

4. Check if duplicate element present ?

```js
var containsDuplicate = function (nums) {
  nums.sort((a, b) => a - b);
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] == nums[i - 1]) {
      return true;
    }
  }
  return false;
};
```

5. Return number whose frequency is 1

```js
var singleNumber = function (nums) {
  nums.sort((a, b) => a - b);
  if (nums[nums.length - 1] != nums[nums.length - 2]) {
    return nums[nums.length - 1];
  }
  for (let i = 1; i < nums.length; i += 2) {
    if (nums[i] != nums[i - 1]) {
      return nums[i - 1];
    }
  }
};
```

6.  Intersection of Two Arrays

```js
var intersect = function (nums1, nums2) {
  nums1.sort((a, b) => a - b);
  nums2.sort((a, b) => a - b);
  let nums3 = [];
  let i = 0;
  let j = 0;
  while (i < nums1.length && j < nums2.length) {
    if (nums1[i] == nums2[j]) {
      nums3.push(nums1[i]);
      i++;
      j++;
    } else if (nums1[i] < nums2[j]) {
      i++;
    } else {
      j++;
    }
  }
  return nums3;
};
```

7. Plus one

```python
def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        carry = 1
        i = len(digits)-1
        while i>=0:
            if carry+digits[i] > 9:
                ans.append(0)
            else:
                ans.append(digits[i]+carry)
                carry = 0
            i-=1

        if carry == 1:
            ans.append(1)

        ans.reverse()
        return ans
```

8. move zeros to the end

```js
var moveZeroes = function (nums) {
  let slow = 0;
  for (let fast = 0; fast < nums.length; fast++) {
    if (nums[fast] != 0 && nums[slow] == 0) {
      let temp = nums[fast];
      nums[fast] = nums[slow];
      nums[slow] = temp;
    }
    if (nums[slow] != 0) {
      slow++;
    }
  }
};
```

9. Two Sum

```js
var twoSum = function (nums, target) {
  let d = {};
  let diff = 0;
  for (let i = 0; i < nums.length; i++) {
    diff = target - nums[i];
    if (diff in d) return [d[diff], i];
    else {
      d[nums[i]] = i;
    }
  }
};
```

10. Valid Sudoku

```js

```

11. Rotate Image

```js
var rotate = function (matrix) {
  let temp = 0;
  let temparr = [];
  let i = 0;
  let j = matrix.length - 1;

  while (i < j) {
    temparr = matrix[i];
    matrix[i] = matrix[j];
    matrix[j] = temparr;
    i++;
    j--;
  }

  for (i = 0; i < matrix.length; i++) {
    for (let j = 0; j < i; j++) {
      temp = matrix[i][j];
      matrix[i][j] = matrix[j][i];
      matrix[j][i] = temp;
    }
  }
};
```

# Sorting Algo's

1. Selection Sort

```python
arr = [1,9,2,8,3,7,4,6,5]

i = 0
while i < len(arr):
    min = i
    j = i+1
    while j < len(arr):
        if arr[j] < arr[min]:
            min = j
        j+=1
    arr[i], arr[min] = arr[min], arr[i]
    i+=1

print(arr)
```

2. Bubble Sort

```python
arr = [1,9,2,8,3,7,4,6,5]

i = 0
while i < len(arr):
    j = 0
    while j < len(arr)-1-i:
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        j+=1
    i+=1

print(arr)
```

3. Insertion Sort

```python
arr = [1,9,2,8,3,7,4,6,5]

i = 1
while i < len(arr):
    j = i
    while j>0 and arr[j]<arr[j-1]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j-=1
    i+=1

print(arr)
```

4. Quick Sort

```python
arr = [1,9,2,8,3,7,4,6,5]

def quick(arr, low, high):
    i = low
    j = high
    pivot = arr[low]
    while i<j:
        while (arr[i]<=pivot and i<=high-1):
            i+=1
        while (arr[j]>pivot and j>=low+1):
            j-=1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] =  arr[j], arr[low]
    return j

def quickSort(arr, low, high):
    if low<high:
        pelement = quick(arr, low, high)
        quickSort(arr, low, pelement-1)
        quickSort(arr, pelement+1, high)

quickSort(arr, 0, len(arr)-1)

print(arr)
```

## Strategy for Array -

### Steps to solve array problems -

1. Brute Force Approach
2. Try to find a approach using single loop -
   1. Using extra space
   2. Using 2 pointers
   3. Binary Search

### Medium leetcode questions

1. three-sum ------- two pointer approach
2. container with most water -------- two pointer
3. search in rotated sorted array --------
