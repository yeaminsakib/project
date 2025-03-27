alphabets = 'abcdefghijklmnopqrstuvwxyz'
def encrypt_caesar(num, text):
    result = ''
    for k in text.lower():
        try:
            i = (alphabets.index(k) + num) % 26
            result += alphabets[i]
        except ValueError:
            result += k  # Keep the character as is (e.g., space, punctuation)
    return result.lower()

num = int(input("Please input the shift:\t"))
text = input("Please input the text:\t")
ciphertext = encrypt_caesar(num, text)
print("Encoded text:", ciphertext)
