### Java RSA Encryption

```
import java.math.BigInteger;
import java.security.KeyFactory;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.NoSuchAlgorithmException;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.RSAPrivateKeySpec;
import java.security.spec.RSAPublicKeySpec;
import javax.crypto.Cipher;

public class RSA_Encryption {
    
    public static void main(String[] args) throws Exception {
        // Generate key pair
        KeyPair keyPair = generateKeyPair();

        // Convert keys to their spec form
        RSAPublicKeySpec publicKeySpec = getRSAPublicKeySpec(keyPair.getPublic());
        RSAPrivateKeySpec privateKeySpec = getRSAPrivateKeySpec(keyPair.getPrivate());

        // Encrypt and decrypt message
        String message = "Hello World!";
        byte[] encrypted = encrypt(message, publicKeySpec);
        String decrypted = decrypt(encrypted, privateKeySpec);
        System.out.println("Encrypted: " + new String(encrypted));
        System.out.println("Decrypted: " + decrypted);
    }

    public static KeyPair generateKeyPair() throws NoSuchAlgorithmException {
        KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA");
        keyPairGenerator.initialize(2048);
        return keyPairGenerator.generateKeyPair();
    }

    public static RSAPublicKeySpec getRSAPublicKeySpec(PublicKey publicKey) throws InvalidKeySpecException {
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        return keyFactory.getKeySpec(publicKey, RSAPublicKeySpec.class);
    }

    public static RSAPrivateKeySpec getRSAPrivateKeySpec(PrivateKey privateKey) throws InvalidKeySpecException {
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        return keyFactory.getKeySpec(privateKey, RSAPrivateKeySpec.class);
    }

    public static byte[] encrypt(String message, RSAPublicKeySpec publicKeySpec) throws Exception {
        Cipher cipher = Cipher.getInstance("RSA");
        PublicKey publicKey = KeyFactory.getInstance("RSA").generatePublic(publicKeySpec);
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        return cipher.doFinal(message.getBytes());
    }

    public static String decrypt(byte[] encrypted, RSAPrivateKeySpec privateKeySpec) throws Exception {
        Cipher cipher = Cipher.getInstance("RSA");
        PrivateKey privateKey = KeyFactory.getInstance("RSA").generatePrivate(privateKeySpec);
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        return new String(cipher.doFinal(encrypted));
    }
}
```

### Java 3DES Encryption

```
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class TripleDes_Encryption {
    private static final String ALGORITHM = "DESede";
    private static final String MODE = "ECB";
    private static final String PADDING = "PKCS5Padding";

    public static String encrypt(String message, String key) throws Exception {
        // Create key spec from the provided key
        SecretKeySpec keySpec = new SecretKeySpec(key.getBytes(StandardCharsets.UTF_8), ALGORITHM);

        // Create cipher instance and set encryption mode
        Cipher cipher = Cipher.getInstance(ALGORITHM + "/" + MODE + "/" + PADDING);
        cipher.init(Cipher.ENCRYPT_MODE, keySpec);

        // Encrypt message
        byte[] encrypted = cipher.doFinal(padMessage(message).getBytes(StandardCharsets.UTF_8));

        // Encode encrypted message in base64 for transmission
        return Base64.getEncoder().encodeToString(encrypted);
    }

    public static String decrypt(String encrypted, String key) throws Exception {
        // Create key spec from the provided key
        SecretKeySpec keySpec = new SecretKeySpec(key.getBytes(StandardCharsets.UTF_8), ALGORITHM);

        // Create cipher instance and set decryption mode
        Cipher cipher = Cipher.getInstance(ALGORITHM + "/" + MODE + "/" + PADDING);
        cipher.init(Cipher.DECRYPT_MODE, keySpec);

        // Decode base64-encoded encrypted message
        byte[] decoded = Base64.getDecoder().decode(encrypted);

        // Decrypt message and remove padding
        String decrypted = new String(cipher.doFinal(decoded), StandardCharsets.UTF_8);
        return unpadMessage(decrypted);
    }

    private static String padMessage(String message) {
        int blockSize = 8; // DES block size is 8 bytes
        int padding = blockSize - message.getBytes(StandardCharsets.UTF_8).length % blockSize;
        StringBuilder builder = new StringBuilder(message);
        for (int i = 0; i < padding; i++) {
            builder.append((char)padding);
        }
        return builder.toString();
    }

    private static String unpadMessage(String message) {
        int padding = message.charAt(message.length() - 1);
        return message.substring(0, message.length() - padding);
    }

    // Example usage
    public static void main(String[] args) throws Exception {
        String message = "Hello World!";
        String key = "0123456789abcdef01234567";
        String encrypted = encrypt(message, key);
        System.out.println("Encrypted: " + encrypted);
        String decrypted = decrypt(encrypted, key);
        System.out.println("Decrypted: " + decrypted);
    }
}

```
