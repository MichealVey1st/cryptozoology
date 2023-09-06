def caesar_cipher(text, shift, action='encode'):
    result = ''
    shift %= 26  # Ensure shift is within the alphabet range (0-25)

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()  # Convert to lowercase for easier calculation
            if action == 'encode':
                char_code = ord(char) + shift
            elif action == 'decode':
                char_code = ord(char) - shift
            else:
                raise ValueError("Action must be 'encode' or 'decode'")
            if char_code > ord('z'):
                char_code -= 26  # Wrap around the alphabet
            elif char_code < ord('a'):
                char_code += 26  # Wrap around the alphabet
            char = chr(char_code)
            if is_upper:
                char = char.upper()
        result += char

    return result

# Get user inputs
text = input("Enter the text: ")
shift_amount = int(input("Enter the shift amount (an integer): "))
action = input("Enter 'encode' or 'decode': ").lower()

# Check for valid action input
if action not in ['encode', 'decode']:
    print("Invalid action. Please enter 'encode' or 'decode'.")
else:
    result = caesar_cipher(text, shift_amount, action)
    print("Result:", result)
