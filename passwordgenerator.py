import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits  + special_chars
pwd_length = 8
pwd = ''
 
for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

while True: 
    pwd = ''
    for i in range(pwd_length):
     pwd += ''.join(secrets.choice(alphabet))

    if (any(char in special_chars for char in pwd) and
        sum(char in digits for char in pwd)>=1):
            break 
print(pwd)