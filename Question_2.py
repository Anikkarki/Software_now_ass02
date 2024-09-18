import time
from PIL import Image
import numpy as np

# Generate a number (n) based on the current time
n = (int(time.time()) % 100) + 50
n += 10 if n % 2 == 0 else 0  # Add 10 if the number is even
print("Generated number (n):", n)

# Open the image, modify pixels, and save the output image
image = Image.open('Chapter1.png')
image_array = np.clip(np.array(image) + n, 0, 255)  # Adjust pixels and clip values to 0-255
Image.fromarray(image_array.astype(np.uint8)).save('chapter1out.png')

# Sum all red pixel values in the new image
red_sum = np.sum(image_array[:, :, 0])  # Red channel sum
print("Sum of red pixel values:", red_sum)

#####

def separate_string(s):
    num_str = ''.join([char for char in s if char.isdigit()])  # Extract numbers
    letter_str = ''.join([char for char in s if char.isalpha()])  # Extract letters
    return num_str, letter_str

def convert_even_numbers_to_ascii(num_str):
    even_numbers = [char for char in num_str if int(char) % 2 == 0]  # Filter even numbers
    ascii_values = [ord(char) for char in even_numbers]  # Convert to ASCII decimal values
    return even_numbers, ascii_values

def convert_uppercase_letters_to_ascii(letter_str):
    uppercase_letters = [char for char in letter_str if char.isupper()]  # Filter uppercase letters
    ascii_values = [ord(char) for char in uppercase_letters]  # Convert to ASCII decimal values
    return uppercase_letters, ascii_values

# Example input
s = '56aAww19BN84sktr235270aYmn145ss785fsq31D0'

# Separate the string into number and letter substrings
num_str, letter_str = separate_string(s)

# Convert even numbers to ASCII values
even_numbers, even_ascii = convert_even_numbers_to_ascii(num_str)

# Convert uppercase letters to ASCII values
uppercase_letters, uppercase_ascii = convert_uppercase_letters_to_ascii(letter_str)

# Output
print("Even Numbers:", even_numbers)
print("ASCII Values of Even Numbers:", even_ascii)
print("Uppercase Letters:", uppercase_letters)
print("ASCII Values of Uppercase Letters:", uppercase_ascii)

# Decrypt a Caesar cipher with a given shift
def decrypt_caesar_cipher(cipher_text, shift):
    return ''.join(
        chr((ord(c) - shift - (65 if c.isupper() else 97)) % 26 + (65 if c.isupper() else 97))
        if c.isalpha() else c for c in cipher_text
    )

# Try different shift values to find the correct decryption
cipher_text = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
for shift in range(1, 26):
    print(f"Shift {shift}: {decrypt_caesar_cipher(cipher_text, shift)}")