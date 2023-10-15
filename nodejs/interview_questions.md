# NodeJS Interview Questions

### 1. Mention benefits of using nodeJs ?

Nodejs is asynchronous, single threaded and has event driven architecture because of which there is no buffering.

There is no buffering.

It uses google's V8 JS engine which is super fast.


### 2. Definition of nodeJs ?

It is a javascript runtime environment build on google's V8 engine which allows to write server side applications.

### 3. NodeJs Architecture ?

It is build up on js v8 engine and libuv library

v8 engine - It is used to execute js code.
libuv - responsible for event loop and thread pool.

NodeJs is written in js and c++.

### 4. Node Process and Threads

Nodejs is single threaded. So there is an extra thread pool to offload workload from this single thread. Libuv provides this thread pool which performs heavy tasks.

### 5. NodeJs Event Loop ?

It receives the events, calls the callback functions and offloads the more expensive tasks to thread pool.

### 6. Event loop phases ?

It has basically different callback queues for different type of events.
First is Expired Timer callback, next is I/O polling (network and fs) callbacks, then setImmediate callback, close callbacks, then process.tick() callbacks and in last some other microtask queue like for promises.



### 6. What is V8 engine ?

It is a JS engine that parses and executes js code. It powers chrome. 
Other engines are spider monkey and chakra.


### 7. Just in time compiler in JS ?

Compiler - Source code is converted to machine code first and then executed.
It takes more time but the machine code is optimized and the repeated code is not translated again and again.

Interpreter - Source code is directly converted line by line and executed.
It takes less startup time but it is not optimized.

The JIT compiler is a mix of compiler and interpreter, it has a component called monitor which identifies the code, checks what is more suitable for it and then sends it to interpreter or compiler based on the code.


### 8. What is NPM ?

Node package manager is responsible for downloading the dependencies needed for the project.

### 9. What are dev dependencies ?

Packages that are only required during the development phase are dev dependencies.
We can use --save-dev for it. npm install --save-dev nodemon


### 10. What is typescript ?

It is a superset of js, it allows static type definitions like what type of arguments are to be expected or what type should be returned in a function or the exact shape of an object.


### 11. How nodeJS is asynchronous ?

It does async operations with the help of callbacks, the functions which are passed to another function so that they can be executed after a particular period of time.


### 12. What is event driven architecture ?

1. Event is emitted (setTimeout).
2. Event loop picks the event and the corresponding callback associated with the event.
3. When callstack is free, that callback is called.


### 13. Internally is NodeJS single threaded ?

No, it has a thread pool in libuv, which is used to perform some heavy operations. This thread pool executes tasks parallely in the processors.


### 14. Serverless NodeJs ?

Cloud servers are serverless which means no need to manage infrastructure.


### 15. Objects deep and shallow cloning ?

```js
let obj = {
    layer1: {
        layer2: {
            layer3: {
                name: "Yash",
            }
        }
    }
}

let newObj1 = obj       // Only the reference is copied
let newObj2 = { ... obj }    // Shallow cloning is done, only first layer is different, indepth it is same.
let newObj3 = JSON.parse(JSON.stringify(obj))    // this is one way to separate out the new object completely.
let newObj4 = structuredClone(obj)      // new way to clone, deep cloning Node 17
```


### 16. importing modules ?

So whenever we import modules, first it checks in nodemodules, then one step up and then in the global modules, so if we have a malicious fs module in nodemodules and we don't want to import it, what we want is the core module to be imported, what is to be done is to use node: syntax i.e. const fs = require('node:fs');


### 17. Concurrency Vs Parallelism ?

In concurrency, things works sequentially but the execution is such that it seems like two tasks are going in parallel.
In parallelism, for a given time slice, both the tasks are happening.


### 18. How to build scalable backends ?

1. Horizontal Scaling.
2. Code should be stateless, no single server should contain some kind of local computation, for example authentication at a local level would be a disaster.
3. Using a distributed DB
4. Try to use managed services, like aws s3 and lambda.

