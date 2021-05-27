import webbrowser
import json
import pyaes, pbkdf2, binascii, os, secrets

# Derive a 256-bit AES encryption key from the password
password = input("password? ")
passwordSalt = input("salt? ")
passwordSalt = bytes(passwordSalt, 'utf-8')

key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
print('AES encryption key:', binascii.hexlify(key))
print(str(binascii.hexlify(key)).strip("b'"))
print('AES encryption key:', key)
print(bytes.fromhex(str(binascii.hexlify(key)).strip("b'")))






#iv =  input("iv? ")
#iv = iv.randbits(256)
iv = secrets.randbits(10)
plaintext = input("texto a cifrar? ")

aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext = aes.encrypt(plaintext)
print('Encrypted:', ciphertext)
print('Encrypted:', binascii.hexlify(ciphertext))
print(iv)

aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
decrypted = aes.decrypt(ciphertext)

result = [iv, ciphertext, key]
#print(result)
f = open('Tarea3ConstanzaSepulveda.html','w')

mensaje = """<html>
<head></head>
<body>
    
    <p>Este sitio contiene un mensaje secreto</p>
    <div class="algorithm" id="""+ str(iv) + str(binascii.hexlify(ciphertext)) + str(binascii.hexlify(key))  +""" style="visibility: hidden">
        <p>jhjkhkhk</p>
    </div>

</body>
</html>"""

f.write(mensaje)
f.close()

webbrowser.open_new_tab('Tarea3ConstanzaSepulveda.html')