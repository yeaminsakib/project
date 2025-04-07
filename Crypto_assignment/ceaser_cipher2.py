def encrypt_caesar_v2(shift, text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_index = (alphabet.index(char.lower()) + shift) % 26
            shifted_char = alphabet[shift_index]
            if char.isupper():
                result.append(shifted_char.upper())
            else:
                result.append(shifted_char)
        else:
            result.append(char)  # Keep non-alphabetic characters as they are
    
    return ''.join(result)

shift = int(input("Please input the shift:\t"))
text = input("Please input the text:\t")
encoded_text = encrypt_caesar_v2(shift, text)
print("Encoded text:", encoded_text)
