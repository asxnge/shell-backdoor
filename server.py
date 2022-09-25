import socket

def main():
    host = "127.0.0.1" 
    port = 6500 
 
    s = socket.socket() 
    s.bind((host,port))
 
    s.listen(1)
    print("Waiting for connection...")
    connection, address = s.accept() 
    print("Connection from " + str(address))
    while True:
        try:
            toSend = input("-> ")
            connection.send(toSend.encode()) 
            data = connection.recv(1024).decode() 
            print(data) 
        except:
            break
    print("Connection refused") 
    connection.close()
 
if __name__ == '__main__':
    main()