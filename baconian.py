# Define the Baconian Cipher alphabet
baconian_alphabet = {
    'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA',
    'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB',
    'K': 'ABABA', 'L': 'ABABB', 'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA',
    'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
    'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB', 'Y': 'BBAAA',
    'Z': 'BBAAB',
}

def baconian_encode(text):
    text = text.upper()
    encoded_text = ''

    for char in text:
        if char.isalpha():
            encoded_text += baconian_alphabet[char]
        else:
            encoded_text += char  # Keep non-alphabetic characters as they are

    return encoded_text

def baconian_decode(encoded_text):
    decoded_text = ''
    current_group = ''

    for char in encoded_text:
        if char == ' ':
            decoded_text += ' '
        else:
            current_group += char
            if len(current_group) == 5:
                for letter, code in baconian_alphabet.items():
                    if code == current_group:
                        decoded_text += letter
                        break
                else:
                    decoded_text += current_group  # Keep unrecognized groups
                current_group = ''

    return decoded_text

# Get user input
action = input("Enter 'encode' or 'decode': ").lower()
text = input("Enter the text: ")

if action == 'encode':
    result = baconian_encode(text)
    print("Encoded Text:", result)
elif action == 'decode':
    result = baconian_decode(text)
    print("Decoded Text:", result)
else:
    print("Invalid action. Please enter 'encode' or 'decode'.")
