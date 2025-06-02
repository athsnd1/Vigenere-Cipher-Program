def vigenere_cipher(plaintext, key):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = plaintext.upper()
    key = key.upper()
    cipher_text = ""

    for i in range(len(plaintext)):
        if plaintext[i] not in alphabets:
            cipher_text += plaintext[i]
            continue

        index = alphabets.index(plaintext[i])
        key_index = alphabets.index(key[i % len(key)])
        new_index = (index + key_index) % 26
        cipher_text += alphabets[new_index]

    return cipher_text

plain_text = input("Enter plaintext of your choice: ")
key = input("Enter the key of your choice (must contain only letters of the alphabet): ")
result = vigenere_cipher(plain_text, key)
print(f"The encrypted text is: {result}")
