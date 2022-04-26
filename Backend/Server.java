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
        //ObjectOutputStream outStream = new ObjectOutputStream(socket.getOutputStream());
        InputStream inStream = socket.getInputStream();
        
        boolean flag = true;
        try{

            while(flag){

             String recvImg = inStream.toString();
             if(recvImg == "QUIT")
                 break;
             System.out.println("check 1");
             //byte[] decodedImage = Base64.getDecoder().decode(recvImg);
             byte[] img = inStream.readAllBytes();
             
             FileOutputStream out = new FileOutputStream("img.jpg");
             System.out.println(img);
             //String imgString=Base64.getEncoder().encodeToString(img); 
             out.write(img);
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
