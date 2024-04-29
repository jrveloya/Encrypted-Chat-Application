# Encrypted-Chat-Application

## Overview
The Encrypted Chat Application is a simple chat platform that enables up to four clients to communicate securely through a server. 
The server handles all encryption and decryption of messages, ensuring secure communication between clients. The application is build using Java
 and the project would include the following features:
-Symmetric Encryption
-Multi-Threading
-Message Authentication


## Features
1. **Client-Server Architecture**
The application consists of a server and up to four clients. Clients connect to the server, which manages communication between them.
2. **Encryption and Decryption**
The server encrypts messages before relaying them to the recipient client, ensuring secure communication. Messages are decrypted upon receipt before being displayed.
3. Symmetric Encryption
The application uses AES (Advanced Encryption Standard) in CBC mode for encryption and decryption.

4. **HMAC for Message Integrity**
Messages can include a Message Authentication Code (MAC) to ensure integrity and authenticity, preventing tampering.

5. **Multi-threaded Server**
The server uses multi-threading to manage multiple clients concurrently, allowing for efficient communication.





