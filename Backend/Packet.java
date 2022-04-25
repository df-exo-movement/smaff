// package smaff.Backend;

import java.io.File;
import java.util.Base64;
import java.io.FileInputStream;

public class Packet {
    String message;
    String base64Image;

    public Packet(String message){
        this.message = message;
    }

    public Packet(File file) throws Exception{ //accepts an object of type File and encodes it to a base64 String for storage.
        
        byte[] fileBytes = new byte[(int) file.length()]; //initialize byte array for file

        FileInputStream in = new FileInputStream(file); //create file input stream for input file
        in.read(fileBytes); //read the byte array of the file and store it in the byte array

        this.base64Image = Base64.getEncoder().encodeToString(fileBytes); //encode byte array as base64 string for retrieval
        in.close();
    }

    public String getBase64Image(){
        return this.base64Image;
    }

    public String getPacketMessage(){
        return this.message;
    }
}