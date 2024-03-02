def find_direction(ed, d, matrix, message, fill):
    down = False
    row, col = 0, 0
    res = [] if fill else None
    for char in message if ed else range(message):
        if row == 0:
            down = True
        if row == d - 1:
            down = not down if ed else False

        if fill:
            if matrix[row][col] != '*':
                res.append(matrix[row][col])
                col += 1
        else:
            matrix[row][col] = char if ed else '*'
            col += 1

        if down:
            row += 1
        else:
            row -= 1
    if fill:
        return res


def encrypt_rfc(message, key):
    message = message.replace(" ", "").lower()
    d, r = key

    for _ in range(r):
        matrix = [['\n' for _ in range(len(message))] for _ in range(d)]
        find_direction(1, d, matrix, message, 0)

        result = [matrix[i][j] for i in range(d) for j in range(len(message)) if matrix[i][j] != '\n']
        message = "".join(result)

    return message


def decrypt_rfc(cipher, key):
    d, r = key
    cipher = cipher.replace(" ", "").lower()
    cipher_length = len(cipher)

    for _ in range(r):
        matrix = [['\n' for _ in range(cipher_length)] for _ in range(d)]
        find_direction(0, d, matrix, cipher_length, 0)

        indx = 0
        for i, j in ((i, j) for i in range(d) for j in range(cipher_length)
                     if matrix[i][j] == '*' and indx < len(cipher)): matrix[i][j], indx = cipher[indx], indx + 1

        result = find_direction(0, d, matrix, cipher_length, 1)
        cipher = "".join(result)
    return cipher


while True:
    print('------------------------------------------------------')
    print("Rail Fence Cipher Menu Options")
    print('------------------------------------------------------')
    print('1. Encrypt Text')
    print('2. Decrypt Text')
    print('3. Test 1 (Encryption)')
    print('4. Test 2 (Decryption)')
    print('5. Quit')
    option = int(input("Please select an option:\n"))

    if option == 1:
        pt = input("Please enter the plain text:\n")
        depth = int(input("Please enter the depth of encryption:\n"))
        round = int(input("Please enter the number of encrypt round:\n"))
        encrypted_text = encrypt_rfc(pt, (depth, round))
        print("Encrypted Text:", encrypted_text)
    elif option == 2:
        ct = input("Please enter the cipher text:\n")
        depth = int(input("Please enter the depth of decryption:\n"))
        round = int(input("Please enter the number of decrypt round:\n"))
        decrypted_text = encrypt_rfc(ct, (depth, round))
        print("Decrypted Text:", decrypted_text)
    elif option == 3:
        # Test 1 Encryption
        key_en = (4, 5)  # Depth of 4, repeat 5 times
        text = "CRYPTOLOGY IS THE PRACTICE AND STUDY OF TECHNIQUES FOR SECURE COMMUNICATION IN THE PRESENCE OF THIRD PARTIES CALLED ADVERSARIES"
        encrypted_text = encrypt_rfc(text, key_en)
        print("Encrypted Text:", encrypted_text)
    elif option == 4:
        # Test 2 Decryption
        key_de = (3, 3)  # Depth of 3, repeat 3 times
        encrypted_message = "TPSNIONFRMHANOIREEOIBTSEAKLAPSEHISOBPEGTBRQREPTTMHRTHTTAWE AACTFVAECAOLHANSEEKFHALOITUEEAICNLEYOLTOLEPADFKATATSJMSIINSH ROCTITRIEEAKYNHYUEOTTSTATSIIRSARERUYUEDPCLETEROINEIYEHC"
        decrypted_text = decrypt_rfc(encrypted_message.replace(" ", ""), key_de)
        print("Decrypted Text:", decrypted_text)
    elif option == 5:
        print("Good bye")
        break
    else:
        print("Wrong option")



