import string as st 
lowers = st.ascii_lowercase
uppers = st.ascii_uppercase
special = st.punctuation
numbers = st.digits


def encrypt(message):
    enc_lowers = lowers[5:8] + lowers[20:26] + lowers[0:5] + lowers[17:20] + lowers[8:17]
    enc_uppers = uppers[8:17] + uppers[0:5] + uppers[20:26] + uppers[5:8] + uppers[17:20]
    enc_special = special[20:26] + special [30:32] + special[0:6] + special[10:12] + special[18:20] + special[26:30] + special[6:10] + special[14:18] + special[12:14]
    enc_numbers = numbers[3:6] + numbers[0:3] + numbers[9:10] + numbers[8:9] + numbers[6:8]
    
    print(lowers, uppers, special, numbers)
    print(enc_lowers, enc_uppers, enc_special, enc_numbers)

    output = ''
    for c in message:
        if c.islower():
            pos = lowers.find(c)
            output += enc_lowers[pos]
        elif c.isupper():
            pos = uppers.find(c)
            output += enc_uppers[pos]
        elif c.isdigit():
            pos = numbers.find(c)
            output += enc_numbers[pos]
        else:
            pos = special.find(c)
            output += enc_special[pos]

    return output

if __name__ == '__main__':
    message = input('Enter message to input: ')
    enc = encrypt(message)
    print(f'Encrypted, {enc}')
    dec = encrypt(enc)
    print(f'Decrypted, {dec}')

    

