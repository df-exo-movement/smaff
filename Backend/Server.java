package smaff.Backend;
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
        ObjectInputStream inStream = new ObjectInputStream(socket.getInputStream());

        Packet recvPacket = (Packet)inStream.readObject();
        System.out.println(recvPacket.message);

        if(recvPacket.message.equals("Hello!")){
            Packet packet = new Packet("Hi! - From Server");
            outStream.writeObject(packet);
        }
    serverSocket.close();
    }
}
