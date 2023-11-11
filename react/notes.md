## What is React ?

A JS library for building user interfaces. We write code in a declarative component focused approach.

example - Netflix


>Single Page Application - Server only sends one HTML page and reacts take over and controls the UI. 

>[reactjs official website](https://www.react.dev)


## Why React ?

To make apps more reactive and interactive without any delay or latency, we can use javascript which can manipulate DOM but js has its limits and it works in imperative way. React is a js library which handles all the details behind the scenes and helps the developer focus on the end goal which is to make more modern and complex user interfaces.


## All other options of react

1. Angular <br> It is also component based UI framework but it has more features as compared to react. It is good for large projects

2. Vue <br> It is also component based UI framework and its features are between react and angular.


## Default Exports and Named Exports - 

>If we need to export something by default and only one thing from a file, we can use default exports.<br>

>But if we need to export different properties and methods from the same file, we can use named exports.

```js
// File1 
const defaultExport = ()=>console.log("This is default export");
export default defaultExport

// File2
export const namedExport = ()=>console.log("This is named export");

// File
import de from './File1';
import {namedExport as nE} from './File2';
import * as bundle from './File2';
```

# Getting Inside React

### 1. What are components?

Components are reusable and independent buidling block of any user interface. 

### 2. Why Components ?

They make code reusable and we have separation of concern.

### 3.  What is create-react-app ?

It is a tool which helps us to build and set up react app easily.
> npx create-react-app app-name. [website](https://create-react-app.dev/)

### 4. What were the steps you did to start the react project ?

>install nodejs <br>
command - npm create-react-app myapp<br>
command - cd myapp<br>
command - npm start

### 5. What is JSX ?

Stands for JavaScript XML which is used to write HTML and javascript together. Browser does not understands jsx and thus behind the scenes babel(transpiler) is used to convert the code to javascript at the time of npm start in create-react-app.


### 6. What is the difference between imperative and declarative approach ?

Imperative approach focuses on each and every step to get the final goal.
Whereas Declarative approach just declares the final goal.


### 7. How does React differentiate between custom made Components and normal HTML elements -- Asked frequently in Interview

Custom made components have their first case as upper case whereas normal html elements are lower case.


### 8. Why do we use className and not class in JSX ?

As JSX has both html and javascript, javascript has class as a reserved keyword thus we use className.


### 9. 



