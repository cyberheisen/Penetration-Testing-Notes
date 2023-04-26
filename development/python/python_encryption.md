## Python RSA Encryption
```
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def rsa_encrypt(message):
    # Generate key pair
    key = RSA.generate(2048)

    # Encrypt message using public key
    cipher = PKCS1_OAEP.new(key.publickey())
    encrypted = cipher.encrypt(message.encode('utf-8'))

    # Encode encrypted message in base64 for transmission
    return base64.b64encode(encrypted).decode('utf-8')

def rsa_decrypt(encrypted):
    # Decode base64-encoded encrypted message
    encrypted = base64.b64decode(encrypted)

    # Decrypt message using private key
    key = RSA.generate(2048)
    cipher = PKCS1_OAEP.new(key)
    decrypted = cipher.decrypt(encrypted)

    # Return decrypted message
    return decrypted.decode('utf-8')

# Example usage
message = "Hello, World!"
encrypted = rsa_encrypt(message)
print("Encrypted: " + encrypted)
decrypted = rsa_decrypt(encrypted)
print("Decrypted: " + decrypted)
```
## Python 3DES Encryption

```
from Crypto.Cipher import DES3
import base64

def des3_encrypt(message, key):
    # Pad message to a multiple of 8 bytes
    padded_message = message + ((8 - len(message) % 8) * chr(8 - len(message) % 8)).encode('utf-8')

    # Encrypt message using 3DES
    cipher = DES3.new(key, DES3.MODE_ECB)
    encrypted = cipher.encrypt(padded_message)

    # Encode encrypted message in base64 for transmission
    return base64.b64encode(encrypted).decode('utf-8')

def des3_decrypt(encrypted, key):
    # Decode base64-encoded encrypted message
    encrypted = base64.b64decode(encrypted)

    # Decrypt message using 3DES
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted = cipher.decrypt(encrypted)

    # Unpad decrypted message
    padding = decrypted[-1]
    return decrypted[:-padding].decode('utf-8')

# Example usage
message = "Hello, World!"
key = b"0123456789abcdef01234567"
encrypted = des3_encrypt(message, key)
print("Encrypted: " + encrypted)
decrypted = des3_decrypt(encrypted, key)
```
