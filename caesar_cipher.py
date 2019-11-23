# This program shifts the input message by a letter to the right
# Characters must be:
#   all caps
#   only letters
# example: AVE CAESAR = BWFDBFTBS

message = input('Type message to encrypt: ')

code = ''
for char in message.upper():
    if char == 'Z':
        code += 'A'
    elif not char.isalpha():
        continue
    else:
        code += chr(ord(char)+1)

print(code)