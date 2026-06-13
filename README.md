I make a directory secureChat then I updated my linux and i checked to see the python3 version is there.

<img width="755" height="538" alt="image" src="https://github.com/user-attachments/assets/85c1dcfe-da71-47d4-9b23-dc572ed307bf" />

Then i install the require package Pycryptodome
<img width="751" height="285" alt="image" src="https://github.com/user-attachments/assets/63a390e8-04a3-4a0f-bcbc-280205819b75" />

Then i generate my AES keys
<img width="603" height="253" alt="image" src="https://github.com/user-attachments/assets/ce2bf815-5206-4d73-813f-10b9d31a95dc" />

I create an Encryption module with nano named Crypto.utiles.py
<img width="751" height="627" alt="image" src="https://github.com/user-attachments/assets/336a1df0-7ad8-419d-80da-c065f4699fce" />

I create a Server
<img width="751" height="387" alt="image" src="https://github.com/user-attachments/assets/c7e80020-9b4b-4a73-a5be-00799646812b" />

I create a Client 
<img width="752" height="403" alt="image" src="https://github.com/user-attachments/assets/5c30e605-4895-43ed-874a-9ae4400bb215" />
<img width="750" height="577" alt="image" src="https://github.com/user-attachments/assets/6f80f8fb-2f71-462a-9022-ddcecaf36b74" />

I opened 3 terminals to start my IP address and client 1 & 2 and it is successful
<img width="752" height="402" alt="image" src="https://github.com/user-attachments/assets/9f100fd3-19b5-4678-93d5-61a0c03342f4" />

Then i test if the Ecryption is working
<img width="753" height="298" alt="image" src="https://github.com/user-attachments/assets/c91d4f12-678b-4f9c-b23f-94c74b424e83" />

I viewed the logs 
<img width="647" height="557" alt="image" src="https://github.com/user-attachments/assets/c5f01073-2d34-4308-8006-2461ed49ac3d" />

This project involved developing a secure client-server chat application using Python. TCP sockets were implemented to enable reliable communication between clients and the server. To ensure confidentiality, all messages were encrypted using AES-256 symmetric encryption before transmission and decrypted upon reception. A pre-shared key mechanism was used for secure communication, while a unique Initialization Vector (IV) was generated for each message to improve cryptographic security.
The server was designed to support multiple clients concurrently using Python threading, allowing several users to communicate simultaneously. Message logging was also implemented to record chat activity for monitoring and auditing purposes.
Testing confirmed that messages were transmitted in encrypted form across the network and successfully decrypted by the server. The project provided practical experience in network programming, cryptography, socket communication, concurrent programming, and secure application development.
