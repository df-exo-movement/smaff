package smaff.Backend;

import java.io.Serializable;
import java.util.Base64;

public class Packet implements Serializable {
    String message;
    byte[] src;
    String base64Image;

    public Packet(String message){
        this.message = message;
    }

    public Packet(File file){
        this.src = file;
        base64Img = Base64.getEncoder().encodeToString(src);
    }

    public String getBase64Image(){
        return base64Image;
    }
}