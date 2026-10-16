import java.util.Scanner;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
public class AES{
    public static void main(String[] args) throws Exception{
        Scanner sc= new Scanner(System.in);
        String text=sc.nextLine();
        String key="1234567890123456";
        SecretKeySpec secretKey=new SecretKeySpec(key.getBytes(),"AES");
        Cipher cipher=Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE,secretKey);
        byte[] encrypted= cipher.doFinal(text.getBytes());
        System.out.println("Encypted:"+java.util.Base64.getEncoder().encodeToString(encrypted));
        cipher.init(Cipher.DECRYPT_MODE,secretKey);
        byte[] decrypted=cipher.doFinal(encrypted);
        System.out.println("Decrypted:"+new String(decrypted));
    }
}