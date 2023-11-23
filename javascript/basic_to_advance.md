# Basics of Web Development

## HTML Tags

1. p
2. img src
3. a href
4. h1-h6
5. hr, br
6. pre  (preserves all spaces and line breaks)
7. p style=color:blue
8. p style=font-family:courier
9. p style="text-align:center
10. p style=font-size:50px
11. p style=background-color:yellow
12. strong  (bold)
13. em      (emphasize)
14. mark
15. sub     (subscript)
16. del     (strikethrough)
17. q       (quotation marks)
18. <blockquote cite="http://www.worldwildlife.org">blockquote cite</blockquote>

19. <p><abbr title="Yash Gupta"> YG</abbr> was founded in 1999.(abbr tag)</p> 

20. inside head style tag can be used to add css

23. CSS can be implemented in 3 ways - 
    Inline, Internal, External

24. CSS properties <br>
    color<br>
    font-family<br>
    font-size<br>
    text-align<br>
    background-color<br>
    text-decoration<br>

### HTML Forms
```html
<form>
    <label for='Name'>Name</label><br>
    <!-->for of label should be equal to id of input to bind them<-->
    <input type='text' name='name'>
    <!-->Name attribute is used to extract the input at the backend<-->
    <input type='radio'>
    <input type='checkbox'>
    <input type='submit'>
    <!-->Submit button submits form data to form handler defined in action attribute of form<-->
    <input type='button' value="OK">
</form>
```


# Javascript

## Basics of Array

```js
let names = ['yash', 'sourabh', 'shivam', 'durgesh']
```
### Methods

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




## Basics of Strings

```js
let s = 'Yash Gupta'
```

### String Methods
```js
let length = s.length;

let part = s.slice(0, 5)

let part2 = s.substring(0,5) //No negative index

let part3 = s.substr(0, 5)  //5 represents length of string

let newS = s.replace('a', 'x');

let newS = s.replaceAll('a', 'x');

let s1 = s.toUpperCase();

let s2 = s.toLowerCase();

let newWord = s.concat(' 24');

let trimedS = s.trim();

let trimedStart = s.trimStart();

let trimedEnd = s.trimEnd();

let c = s.charAt(0);

let arr = s.split('');
```




## Objects

```js
const yash = {
    nature: 'hardworking',
    dreams: 'big',
    hobby: 'to help others',
    printDetails: ()=>{
        console.log(`${this.nature}, ${this.dreams}`)
    }
}

console.log(yash.dreams);

console.log(yash['dreams']);

yash.printDetails()
```


### Destructuring

1. Arrays - <br>
```js
let arr = [1,2,3,4,5];

let [a, b] = arr;

console.log(a, b);
```
2. Objects - <br>
```js
let obj = {name:'Yash'}

let {name} = obj
```

3. Rest Operator - <br>
```js
function add(...args){
    let sum = 0
    for (i of args){
        sum+=i
    }
    return sum;
}
console.log(add(1,2,3,4,5,6,7,8,9,10))
```

4. Spread Operator - <br>
```js

let a1 = [1,2,3];
let a2 = [4,5,6];
let a3 = [...a1, ...a2];
```

## Functions

1. Function Declaration
```js
function details(){
    let name = "Yash";
}
```

2. Function Expression
```js
let details = function(){
    let name = "Yash";
}

```

### Functional Constructor

```js
function Properties(type, length, age){
    this.type = type;
    this.length = length;
    this.age = age
}

const tree1 = new Properties('mango', 50, 200)

console.log(tree1.age)
```




## ES6 Classes


### Static Variables

### Inheritance




## Window Object and Events




## DOM Manipulation


## Local Storage



## Basics of Linked List







    



