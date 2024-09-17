# Question 3

# Below is the final output after the code is decrypted
# Further, we have attached the code(as comment) that explains how we used Ceaser cipher for decryption

global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers()  # Fixed function call

def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable

modify_dict()  # Fixed function call

def update_global():
    global global_variable
    global_variable += 10 

for i in range(5):
    print(i)
    i += 1

if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")  # Fixed typo

if 5 not in my_dict:  # Added missing colon
    print("5 not found in the dictionary!")  # Fixed typo

print(global_variable)
print(my_dict)
print(my_set)






'''def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text


key = 13   # Using the key from previous answer
            # Encrypted code below
original_code = """                    
tybony_inevnoyr = 100
zl_qvpg = {'xrl1' : 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahzoref = [1, 2, 3,4,5]

    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inevnoyr)
        ybpny_inevnoyr -= 1

    erghea ahzoref

zl_frg = {1,2,3,4,5,5,4,3,2,1}
erfhyg = cebprff_ahzoref{ahzoref=zl_frg}

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xrl4'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10 

sbe v va enatr(5):
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:
    cevag("Pbaqvgvba zrgl!")

vs 5 abg va zl_qvpg
    cevag("5 abg sbhaq va gur qvpgvbael!")

cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
"""
# Encrypt the code using the key
encrypted_code = encrypt(original_code, key)
print(encrypted_code)

'''