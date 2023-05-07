#Transmissor

def convert_ASCII(message):
    converted_code = []
    for letter in message:
        converted_code.append(ord(letter))
    return converted_code

def checksum(converted_code, message):
    sum = 0
    for asc in converted_code:
        sum = sum + asc
    last_digit = chr(sum % 127)
    code = message + last_digit
    return code

message = input("\nInsira a mensagem: ")
print("Mensagem com CDE: ", checksum(convert_ASCII(message), message))

#Meio de Transmissão

import random

noise_prob = 0.3 #30% de probabilidade de erro
noisy_message = ''
for c in message:
    if random.random() < noise_prob:
        noisy_message += chr(random.randint(0, 127))
    else:
        noisy_message += c

#Receptor

print("Mensagem recebida pelo receptor: ", (checksum(convert_ASCII(noisy_message), noisy_message)))
if ((checksum(convert_ASCII(message), message)) == (checksum(convert_ASCII(noisy_message), noisy_message))):
    print("Não foi encontrado nenhum erro na transmissão!")
else:
    print("Foi encontrado erro na transmissão!")