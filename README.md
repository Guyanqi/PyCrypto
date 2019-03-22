# PyCrypto

Library of cryptography algorithms written in Python3. 

**Please note that this is under development and is not ready for production!**    
**Official document appear soon ...**

## Cryptography Algorithms Support table

| Algorithm | Library | REST API |
|:---------:| :------:| :-------:|
| Caeser | Yes  | No        |
| DES | Yes  | No        |
| AES | Yes  | No        |
| MD5 | Yes  | No       |
| SHA | Yes  | No       |
| HMAC | Yes  | No       |
| RSA | Yes  | No       |
| Diffie-Hellman | Yes  | No       |
| Elliptic-Curve  | Yes  | No       |
| Blowfish| No  | No        |
| Twofish | No  | No      |

## Current Features

+ Support cipher hashing algorithms  
+ Support basic cryptography algorithms   
+ Support Test and Usage Examples   

## TO APPEAR SOON

+ Integration for Flask and Django
+ REST API
+ Test module migrated to unittest
+ Deployment Support on multi-core systems

## Install & Download  
```bash
git clone https://github.com/Guyanqi/PyCrypto  
```
## Usage
```bash
import PyCrypto
enc = PyCrypto.cipher.caeser(msg, key, flag)
```  

## Compiling instructions

Download and install Python3 for your platform.

## Contribution

Please feel free to submit any pull requests or suggest any desired features to be added.  
You are welcome to star or fork this repository.  

## Copyright
Feel free to use it. 
