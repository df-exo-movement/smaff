package smaff.Backend;

import java.io.Serializable;
import java.util.Base64;

public class Packet implements Serializable {
    String message;
    byte[] src;

    public Packet(String message){
        this.message = message;
    }

    public Packet(File file){
        this.src = file;
        rawFile = Base64.getEncoder().encodeToString(src);
    }
}