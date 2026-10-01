def cipher(original_text):
    space_positions = []
    ciphered_chars = []
    
    for idx, char in enumerate(original_text):
        if char == ' ':
            space_positions.append(idx)
        else:
            ciphered_chars.append(char.upper())
    
    ciphered_text = ''.join(ciphered_chars)
    
    if len(ciphered_text) > 140:
        raise ValueError("Message exceeds the maximum 140-letter limit.")
    
    return ciphered_text, space_positions


def decipher(ciphered_text, space_positions):
    original_length = len(ciphered_text) + len(space_positions)
    result = [''] * original_length
    
   
    for pos in space_positions:
        if pos < 0 or pos >= original_length:
            raise IndexError("Invalid space position: out of bounds.")
        result[pos] = ' '
    

    cipher_ptr = 0
    is_first_letter = True 
    
    for i in range(original_length):
        if result[i] == ' ':
            continue
        
        if is_first_letter:
            result[i] = ciphered_text[cipher_ptr].upper()
            is_first_letter = False
        else:
            result[i] = ciphered_text[cipher_ptr].lower()
        
        cipher_ptr += 1
    
    return ''.join(result)


original_message = "The world population is increasing rapidly"


ciphered_text, space_indices = cipher(original_message)
print("Ciphered text:", ciphered_text)
print("Space positions:", space_indices)


deciphered_text = decipher(ciphered_text, space_indices)
print("Deciphered text:", deciphered_text)

# Github link: https://github.com/none653/ssw-540