# Expense Tracker 

https://finance-tracker-6m0j.onrender.com

## Database 

1. Entities - User, Order, expense, forgotPassword

2. Attributes of each property - 

User - Id, name, email, password, isPremium

Order - Id, orderId, paymentId, status

Expense - Id, price, description, category

ForgotPassword - uuid, userId, isActive


## Flow of the Project 

### 1. Flow

> Execution starts with app.js

> app.js refers to different routes.


## Important questions

### 1. body parser -
 

### 2. cors
Cross-Origin Resource Sharing (CORS) is an HTTP-header based mechanism that allows a server to indicate any origins (domain, scheme, or port) other than its own from which a browser should permit loading resources.

### 3. dotenv

### 4. app.use(express.static("public"));

### 5. What is sequelize ?

### 6. Morgan and Helmet ?

### 7. express.Router();




# Group Chat Application

## Websockets

> It is a bidirectional full duplex protocol for communication between client and server

> Uses - Chatting, notification, live feed, multiplayer gaming, show client progrss.


### What was before websockets, why need websockets ?

Http protocol is used to transfer data between client and server. Client opens a tcp connection, sends request to the server, and server responds to all the requests of client and then the connection is closed.

> Http connection is stateless.

Websockets were introduced for bidirectional communication which Http could not provide, first there is a ws handshake between client and server (the client sends http request with a special 'upgrade' header, and in response the server sends response with switched protocol) and then the communication starts.

> It is a stateful connection because the client and server knows each other.
(horizontal scaling is difficult in stateful connection because the server is connected to the clients, once server closed, all clients dead.)




> More project idea for backend development - 
 - real time communication
 - npm package
 - CLI tool
 - clone website


