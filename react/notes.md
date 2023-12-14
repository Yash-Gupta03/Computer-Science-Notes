## What is React ?

A JS library for building user interfaces. We write code in a declarative component focused approach.

example - Netflix

> Single Page Application - Server only sends one HTML page and reacts take over and controls the UI.

> [reactjs official website](https://www.react.dev)

## Why React ?

To make apps more reactive and interactive without any delay or latency, we can use javascript which can manipulate DOM but js has its limits and it works in imperative way. React is a js library which handles all the details behind the scenes and helps the developer focus on the end goal which is to make more modern and complex user interfaces.

## All other options of react

1. Angular <br> It is also component based UI framework but it has more features as compared to react. It is good for large projects

2. Vue <br> It is also component based UI framework and its features are between react and angular.

## Default Exports and Named Exports -

> If we need to export something by default and only one thing from a file, we can use default exports.<br>

> But if we need to export different properties and methods from the same file, we can use named exports.

```js
// File1
const defaultExport = () => console.log("This is default export");
export default defaultExport;

// File2
export const namedExport = () => console.log("This is named export");

// File
import de from "./File1";
import { namedExport as nE } from "./File2";
import * as bundle from "./File2";
```

# Getting Inside React

### 1. What are components?

Components are reusable and independent buidling block of any user interface.

### 2. Why Components ?

They make code reusable and we have separation of concern.

### 3. What is create-react-app ?

It is a tool which helps us to build and set up react app easily.

> npx create-react-app app-name. [website](https://create-react-app.dev/)

### 4. What were the steps you did to start the react project ?

> install nodejs <br>
> command - npm create-react-app myapp<br>
> command - cd myapp<br>
> command - npm start

### 5. What is JSX ?

Stands for JavaScript XML which is used to write HTML and javascript together. Browser does not understands jsx and thus behind the scenes babel(transpiler) is used to convert the code to javascript at the time of npm start in create-react-app.

### 6. What is the difference between imperative and declarative approach ?

Imperative approach focuses on each and every step to get the final goal.
Whereas Declarative approach just declares the final goal.

### 7. How does React differentiate between custom made Components and normal HTML elements -- Asked frequently in Interview

Custom made components have their first case as upper case whereas normal html elements are lower case.

### 8. Why do we use className and not class in JSX ?

As JSX has both html and javascript, javascript has class as a reserved keyword thus we use className.

### 9. What are props in react ?

Like we use parameters and arguments in functions, we use props to transfer data from one component to another.

### 10. What is props.children ?

The value of props.children will be all content between opening and closing custom component. It is used when we create a wrapper component.

> Instead of div, we can create our own custom wrapper component with our own styling.

### 11. How event listeners are used in React ?

```js
<button onClick={deleteExpense}>Delete</button>
```

### 12. How react components are executed (rendered) ?

All the components are functions only, and initially when the application starts all the component (functions) are executed in the beginning and later whenevere we change any value of variable, the functions are not again executed, thus value og title does not change.

### 13. What is useState ?

With the help of useState, we can change the values in component and rerender them so that the user interface can become interactive and can respond to changes.

### 14. Syntax of useState ?

```js
import { useState } from "react";

const [amount, setAmount] = useState(props.amount);

const ExpenseAmount = () => {
  setAmount(5000);
};
```

### 15. Can we use single state or multiple states ?

Both the scenarios are valid, when we use multiple states it looks like

```js
const [title, enteredTitle] = useState("");
const [date, enteredDate] = useState("");
const [amount, enteredAmount] = useState("");

const titleHandler = (event) => {
  console.log(event.target.value);
  enteredTitle(event.target.value);
};

const amountHandler = (event) => {
  console.log(event.target.value);
  enteredAmount(event.target.value);
};
```

and when we use single state, it changes to be like

> Use a function within updatedValues because when our new state depends on our prevSatate, state updation is an asyn operation and by using a function, react ensures prevState values are always in sync.

```js
const [values, updatedValues] = useState({ title: "", date: "", amount: "" });

const titleHandler = (event) => {
  updatedValues((prevState) => {
    return { ...prevSatate, title: event.target.value };
  });
};
```

### 16. How child to parent component communication work ?

The parent passes function as an attribute along with the component and the child calls the function along with the data to be passed as a parameter, the function gets executed in the parent component and it collects the data from the parameter within the function.

### 17. JSX limitations ?

Can have only one root jsx element <br>
We can wrap elements in div but the problem is the final code will have a lot of div's around. <br>
We can use a wrapper component to solve this problem. <br>
<React.Fragment> is a tag we can use or <> simply this works as wrapper tag.

### 18. What are refs ?

### 19. useEffect ?

It is a hook used to perform side effect tasks like sending http request, storing in local storage etc. useEffect takes one cb function and a dependency array and whenever there are changes in the dependency variables of array, the useEffect cb function gets executed.

### 20. useReducer() ?
