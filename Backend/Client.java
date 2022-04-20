package smaff.Backend;
import java.net.Socket;
import java.io.*;
import java.util.Scanner;

public class Client{
    public static final int PORT = 3000;
    public static void main(String[] args) throws Exception{
        new Client();
    }
    
    public Client() throws Exception{
        boolean flag = true;
        Socket socket = new Socket("127.0.0.1", PORT);
        
        ObjectOutputStream outStream = new ObjectOutputStream(socket.getOutputStream());
        ObjectInputStream inStream = new ObjectInputStream(socket.getInputStream());
        Scanner sc = new Scanner(System.in);
        
        try{
            while(flag){
                String msg = sc.nextLine();
                if(msg == "QUIT"){
                    Packet packet = new Packet(msg);
                    outStream.writeObject(packet);
                    System.exit(0);
                    }

                Packet packet = new Packet(msg);
                outStream.writeObject(packet);

                for(int i =0; i < 10; i++){
                Packet recvPacket = (Packet)inStream.readObject();
                System.out.println(recvPacket.message);
                }
            } 
        }
        catch(Exception e){
        System.out.println("Server Closed by Client");
        socket.close();
        outStream.close();
        System.exit(0);
        }
    }
}