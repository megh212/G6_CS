# This is basically code for encryption,decryption does by using cryptography encryption algorithm.
# This code is written by G.Naveen
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.DESKeySpec;
import java.util.Base64;
import java.util.Scanner;

public class DESInputEncryptionDecryption {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter text to encrypt: ");
        String plainText = scanner.nextLine();

        System.out.print("Enter DES key (8 characters) for encryption: ");
        String desKeyEncryption = scanner.nextLine();

        if (desKeyEncryption.length() != 8) {
            System.out.println("Please enter a key of 8 characters for DES encryption.");
            return;
        }

        byte[] desKeyBytesEncryption = desKeyEncryption.getBytes();
        DESKeySpec desKeySpecEncryption = new DESKeySpec(desKeyBytesEncryption);
        SecretKeyFactory keyFactoryEncryption = SecretKeyFactory.getInstance("DES");
        SecretKey secretKeyEncryption = keyFactoryEncryption.generateSecret(desKeySpecEncryption);

        Cipher cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");

        cipher.init(Cipher.ENCRYPT_MODE, secretKeyEncryption);
        byte[] encryptedBytes = cipher.doFinal(plainText.getBytes());
        String encryptedText = Base64.getEncoder().encodeToString(encryptedBytes);
        System.out.println("Encrypted Text: " + encryptedText);

        System.out.print("\nEnter DES key (8 characters) for decryption: ");
        String desKeyDecryption = scanner.nextLine();

        if (desKeyDecryption.length() != 8) {
            System.out.println("Please enter a key of 8 characters for DES decryption.");
            return;
        }

        byte[] desKeyBytesDecryption = desKeyDecryption.getBytes();
        DESKeySpec desKeySpecDecryption = new DESKeySpec(desKeyBytesDecryption);
        SecretKeyFactory keyFactoryDecryption = SecretKeyFactory.getInstance("DES");
        SecretKey secretKeyDecryption = keyFactoryDecryption.generateSecret(desKeySpecDecryption);

        cipher.init(Cipher.DECRYPT_MODE, secretKeyDecryption);
        byte[] decryptedBytes = cipher.doFinal(Base64.getDecoder().decode(encryptedText));
        String decryptedText = new String(decryptedBytes);
        System.out.println("Decrypted Text: " + decryptedText);

        scanner.close();
    }
}