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
