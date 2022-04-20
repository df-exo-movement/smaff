package smaff.Backend;
import java.net.Socket;
import java.io.*;

public class Client{
    public static final int PORT = 3000;
    public static void main(String[] args) throws Exception{
        new Client();
    }
    
    public Client() throws Exception{
        Socket socket = new Socket("127.0.0.1", PORT);
        
        ObjectOutputStream outStream = new ObjectOutputStream(socket.getOutputStream());
        ObjectInputStream inStream = new ObjectInputStream(socket.getInputStream());

        Packet packet = new Packet("Hello!");
        outStream.writeObject(packet);

        Packet recvPacket = (Packet)inStream.readObject();
        System.out.println(recvPacket.message);

        socket.close();
        outStream.close();
    }
}