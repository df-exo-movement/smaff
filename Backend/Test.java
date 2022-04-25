import java.util.*;
import java.io.*;
import java.net.NetworkInterface;

public class Test {
    public static void main(String[] args) throws Exception{
        File file = new File("./index.jpg"); //grab file

        byte[] fileBytes = new byte[(int) file.length()]; //convert file to byte array
        
        FileInputStream myFile = new FileInputStream(file);
        myFile.read(fileBytes); 

        System.out.println(fileBytes);

        String base64Img = Base64.getEncoder().encodeToString(fileBytes); //encode byte array as base64

        System.out.println(base64Img.length()); //telemetry
        myFile.close();

        byte[] decodedImage = Base64.getDecoder().decode(base64Img); //decode base64 image to byte array

        FileOutputStream outFile = new FileOutputStream(".newImage.jpg"); //write byte array to new file
        outFile.write(decodedImage);

        outFile.close();

    }
}
