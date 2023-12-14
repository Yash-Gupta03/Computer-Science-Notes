### Important Terms

1. Vulnerability
2. Backdoors
3. Denial of Service
4. Direct-access
5. EavesDropping
6. Spoofing
7. Tampering
8. Repudiation
9. Information Disclosure
10. Elevation of privilege
11. Exploits
12. Indirect Attacks
13. Firewalls
14. CIA
15. Types of Attack 1. Active 2. Passive

16. Cryptography
    1. Substitution Cipher
    2. Transposition Cipher
    3. Symmetric Key cryptography(private key)
    4. Assymetric Key Cryptography(public key)
17. Hashing
18. One way hash functions
19. Malicious Code 1. Trojan Horse 2. Logic Bomb 3. Trapdoor or backdoor 4. Worm 5. Virus 6. Time Bomb 7. Rabbit

20. Digital Signatures
21. Threads in Network
22. Intrusion Detection System
23. Legal Devices 1. Copyright 2. Patent 3. Trade Secrets
    <br>

[Cyber Security Full Course for Beginner
](https://www.youtube.com/watch?v=U_P23SqJaDc)

### 1. Surface level Demystifying computer systems

4 layers of computer system -

1. User
2. Hardware
3. Operating System
4. Applications

> Computer Starts -
> power button -> Load BIOS -> Boot Code -> Load Operating System -> Load autostart apps

> Operating system works as an interface between apps and hardware

### Breaking Down Computer Networks

1. When two or more than two computers need to communicate to share data, that is computer network. Internet is the biggest example of computer network.

2. There needs to be some set of rules for this communication to happen, and this rules are called protocols

3. Every device on the internet has its own unique IP address.

4. Information Flow over a network <br>
   Alice -> small Internet Service Provider(ISP) -> medium ISP -> Large ISP -> medium ISP -> small ISP -> BOB

5. IP addresses can be static and dynamic, DHCP server is used for dynamic IP address, example a coffee shop router can dynamically assign IP addresses throughout the day for there customers. IP addresses can be private or public.

6. DNS servers are used to convert domain names into IP addresses.

### Passwords

Passwords are used to safeguard the data and only allow the user which own the data.
Passwords are saved on the servers using hash functions which are irreversible.

Passwords Attacks -

1. Phishing
2. Social Engineering
3. Key Logging
4. Wireless sniffing
5. Brute Force Guessing
6. Dictionary Attack

### Emails

They use SMTP protocol

Threads -

1. Eaves Dropping
2. Phishing
3. Spoofing
4. Malicious Email Attachments

### Attacks

1. Man in the middle
2. DDOS
3. Phishing
4. Password Attack
5. Malware attack
6. SQL injection attack

### Basics of AWS

1. Robomaker
2. IOT core
3. Elastic Cloud Computing
4. Elastic Load Balancing
5. Cloud Watch, cloud trail (monitoring service)
6. Auto Scaling
7. BeanStalk - PaaS, Abstraction over all lower level pieces
8. Lambda - Function as a service, serverless computing
9. Outpost - run aws on your own server
10. ECS - Container service for docker
11. Simple Storage Service
12. Glacier
13. Block Storage
14. Dynamo DB
15. Document DB
16. RDS
17. Aurora
18. IAM
19. Cognito
20. Simple Notification service
21. Simple Email Service
22. Cloud Formation - create template based on infrastructure using json
23. Budget
24. Route53 - DNS service used to route user request to apps running on aws

Route53 ->(API Gateway) -> (cognito [user pool]) -> EC2, ECS, Lambda -> Elastic Cache(radis), Aurora, RDS, DynamoDB

### Basics of Cloud Security

Concerns -
Delivering right service and right data to the right identity.
Implement authorization and authentication.
Proactively preventing threads.

3 levels of responsibility for security
User secures - Authorization, Authentication and Identification(Application)
Cloud Secures - Platform security

Access Risks
Data Risks

### Basics of AWS security
