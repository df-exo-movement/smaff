// package smaff.Backend;
import java.net.*;
import java.util.*;
import java.io.*;

public class Server {
    public static final int PORT = 3000;
    
    public static void main(String[] args) throws Exception{
        new Server();
    }

    public Server() throws Exception{
        ServerSocket serverSocket = new ServerSocket(PORT);
        System.out.println("[SERVER UP] Server is running on port " + PORT);
        Socket socket = serverSocket.accept();
        ObjectOutputStream outStream = new ObjectOutputStream(socket.getOutputStream());
        InputStream inStream = socket.getInputStream();
        
        boolean flag = true;
        try{
        while(flag){
         String recvImg = inStream.toString();
         if(recvImg == "QUIT")
             break;
        
         byte[] decodedImage = Base64.getDecoder().decode(recvImg);
         FileOutputStream out = new FileOutputStream("img.jpg");
         out.write(decodedImage);
         out.close();
        
        }
    }
    catch(Exception e){
    System.out.println("[ERROR] Client Forcibly Disconnected");
    serverSocket.close();
    System.exit(0);
    }
    }
}
