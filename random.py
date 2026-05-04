# my own cipher (in progress)
def custom_cipher(text, key):
    # This cipher shifts vowels forward by key, consonants backward by key, digits by key*2, others unchanged
    vowels = 'aeiou'
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if char.lower() in vowels:
                shifted = chr((ord(char) - base + key) % 26 + base)
            else:
                shifted = chr((ord(char) - base - key) % 26 + base)
            result.append(shifted)
        elif char.isdigit():
            shifted = chr((ord(char) - ord('0') + key * 2) % 10 + ord('0'))
            result.append(shifted)
        else:
            result.append(char)
    return ''.join(result)

def custom_decipher(text, key):
    vowels = 'aeiou'
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if char.lower() in vowels:
                shifted = chr((ord(char) - base - key) % 26 + base)
            else:
                shifted = chr((ord(char) - base + key) % 26 + base)
            result.append(shifted)
        elif char.isdigit():
            shifted = chr((ord(char) - ord('0') - key * 2) % 10 + ord('0'))
            result.append(shifted)
        else:
            result.append(char)
    return ''.join(result)

# Example usage:
text = input("Enter text to encrypt: ")
shift = int(input("Enter shift value: "))

custom_encrypted = custom_cipher(text, shift)
print(f"Custom cipher text: {custom_encrypted}")

custom_decrypted = custom_decipher(custom_encrypted, shift)
print(f"Decrypted text: {custom_decrypted}")