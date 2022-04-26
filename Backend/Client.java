// package smaff.Backend;
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
        
        OutputStream outStream = socket.getOutputStream();
        InputStream inStream = socket.getInputStream();
        try{
        while(flag){
            // String msg = sc.nextLine();
            // if(msg == "QUIT"){
            //     Packet packet = new Packet(msg);      TEST CODE FOR CLEAN EXIT
            //     outStream.writeObject(packet);        
            //     System.exit(0);
            // }
            System.out.println("Make a selection. 1 = Quit, 2 = Send Image");
            Scanner sc = new Scanner(System.in);
            String choice = sc.nextLine();
            
            switch(choice){
                case "1":
                    Packet packet = new Packet("QUIT");
                    outStream.write(packet.getPacketMessage());     
                    sc.close();   
                    System.exit(0);

                
                case "2":
                    //Scanner temp = new Scanner(System.in);
                    System.out.println("Enter a file path");
                    String filePath = sc.nextLine();

                    File file = new File(filePath);
                    Packet imgpacket = new Packet(file);
                   // outStream.writeObject(imgpacket.getBase64Image());
                    System.out.println(imgpacket.getBase64Image());

            }

            //Packet packet = new Packet(msg);
            //outStream.writeObject(packet);

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