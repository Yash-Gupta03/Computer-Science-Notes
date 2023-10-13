# Arrays in Python
## Definition 
Collection of elements stored in contiguous memory location.

```names = ['yash', 'sourabh', 'shivam', 'durgesh']```

## Methods
<details>
<summary> Length of array ?</summary>

```x = len(names)```
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

# Arrays in Javascript

```js
let names = ['yash', 'sourabh', 'shivam', 'durgesh']
```

## Methods

<details>
<summary> Length of array ?</summary>

```js
let x = names.length;
```
</details>

<details>
<summary> Looping in general in js ?</summary>

```js
let names = ['yash', 'sourabh', 'shivam', 'durgesh']
for (i of names){
    console.log(i);
}
```

```js
for (let i=0; i<10; i++){
    console.log(i);
}
    
```

```js
names.forEach((name)=>{
    console.log(name);
})
```
</details>

<details>
<summary> Add elements in array ?</summary>

```js
let names = ['yash', 'sourabh', 'shivam', 'durgesh']
names.push('Rohan') # Adds name at the end

names.unshift('Kshitij') # Adds at front
```
</details>

<details>
<summary> Delete Elements from array ?</summary>

```js
names.pop() # pops last element

names.remove(element) #removes that element

names.shift() # removes from front

delete names[0] //leaves holes
```
</details>

<details>
<summary> slice and splice ?</summary>

```js
newnames = names.slice(0,2);

deletedNames = names.splice(start, deleteElementCount, newElements... )
```
</details>

<details>
<summary> All other methods ?</summary>

```js
x = names.toString() //converts array to string

names.sort('yash') //works well in alphabets

values.sort((a,b)=>a-b) //in case of numeric values use compare function

new_name = names.concat('Anushka') // returns a copy

names.reverse();

subarrays.flat();

let str = names.join('and');
```
</details>

<details>
<summary> Map, Filter, Reduce ?</summary>

```js
mappedNames = names.map((name)=>{
    return (name+'sir');
})

filteredNames = names.filter((name)=>{
    if (name == 'yash') return name;
})

reducedNumbers = numbers.reduce((sum, x)=>{
    return sum+=x;
})

```
</details>


# Array Easy Practice Questions
1. Remove Duplicates from Sorted Array

> compare elements, increment only when comparison is not equal

```js
var removeDuplicates = function(nums) {
    let i = 1;
    while (i < nums.length){
        if (nums[i] == nums[i-1]){
            nums.splice(i-1, 1);
        }else{
            i+=1
        }
    }
    return nums.length; 
};
```

2. Best Time to Buy and Sell Stock II

> subtract adjacent value and add to total when i+1 index value is greater than ith value

```js
var maxProfit = function(prices) {
    let i = 1;
    let total = 0;
    while (i<prices.length){
        if (prices[i] > prices[i-1]){
            total+=(prices[i]-prices[i-1]);
        }
        i++;
    }
    return total    
};
```

3. Rotate Array by k steps towards right

> using reverse technique, 
if reversing towards right then first reverse last k elements, then first n-k, then the whole array.

>if reversing towards left then first reverse first k elements, then last n-k, then the whole array.


```js
var rotate = function(nums, k) {
    let i,j, temp;
    let n = nums.length;
    k = k%n;
    for (i = 0, j = n-k-1; i < j; i++, j--){
        temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp
    }
    
    for (i = n-k, j = n-1; i < j; i++, j--){
        temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp
    }
    
    
    for (i = 0, j = n-1; i < j; i++, j--){
        temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp
    }
};
```

4. Check if duplicate element present ?
```js
var containsDuplicate = function(nums) {
    nums.sort((a,b)=>a-b);
    for(let i=1; i<nums.length; i++){
        if (nums[i] == nums[i-1]){
            return true;
        }
    }
    return false;
};

```

5. Return number whose frequency is 1
```js
var singleNumber = function(nums) {
    nums.sort((a,b)=>a-b);
    if (nums[nums.length-1] != nums[nums.length-2]){
        return nums[nums.length-1];
    }
    for(let i=1; i<nums.length; i+=2){
        if (nums[i] != nums[i-1]){
            return nums[i-1];
        }
    }  
};
```

6.  Intersection of Two Arrays
```js
var intersect = function(nums1, nums2) {
    nums1.sort((a,b)=>a-b);
    nums2.sort((a,b)=>a-b);
    let nums3 = [];
    let i = 0;
    let j = 0;
    while (i < nums1.length && j < nums2.length){
        if (nums1[i] == nums2[j]){
            nums3.push(nums1[i]);
            i++;
            j++;
        }else if (nums1[i] < nums2[j]){
            i++;
        }else {
            j++;
        }
    }
    return nums3;
};
```

7. Plus one 
```python
ef plusOne(self, digits: List[int]) -> List[int]:
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

8. 




