# Rail Fence Cipher
The [rail fence cipher](https://en.wikipedia.org/wiki/Rail_fence_cipher), also known as a zigzag cipher, is a classic transposition cipher. Its name comes from its encryption method, which resembles a horizontally railed fence.

## Docker Build
- Install [docker engine](https://docs.docker.com/desktop/) on the computer
  

- Use the command to build docker image
    ```
    bash docker build -t assignmnet2 .
    ```
- Use the command to run image
    ```
    bash docker run -it assignmnet2
    ```

## Rail Fence Cipher Menu Options
#### 1. Encrypt Text
* Input the plain text
* Input the depth of encryption
* Input the number of encrypt round
* Output encrypted text
        
#### 2. Decrypt Text
* Input the cipher text
* Input the depth of decryption
* Input the number of decrypt round
* Output decrypted text

#### 3. Test 1 (Encryption)
* Use the encrypt test example plain text with setting Depth of 4, repeat 5 times to show the result of encrypted text.
#### 4. Test 2 (Decryption)
* Use the decrypt test example cipher text with setting Depth of 3, repeat 3 times to show the result of decrypted text.
#### 5. Quit
* Program close.
