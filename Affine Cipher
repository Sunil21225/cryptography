def affine_encrypt(message, a, b):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((a * (ord(char) - 65) + b) % 26 + 65)
            else:
                encrypted_char = chr((a * (ord(char) - 97) + b) % 26 + 97)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message


def affine_decrypt(ciphertext, a, b):
    decrypted_message = ""
    a_inverse = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inverse = i
            break
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((a_inverse * (ord(char) - 65 - b)) % 26 + 65)
            else:
                decrypted_char = chr((a_inverse * (ord(char) - 97 - b)) % 26 + 97)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message


plaintext = "Hello, World!"
a = 5
b = 8


encrypted_text = affine_encrypt(plaintext, a, b)
print("Encrypted text:", encrypted_text)


decrypted_text = affine_decrypt(encrypted_text, a, b)
print("Decrypted text:", decrypted_text)
