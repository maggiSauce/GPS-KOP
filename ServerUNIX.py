import socket

def runServer():
    host = '127.0.0.1' #localhost
    port = 10000

    # this creates a new socket object
    # .AF_INET specifies using the IPV4 IP address family
    # .SOCK_<> specifies the type of socket
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_SEQPACKET)

    
    # binding the socket to the host and port defined earlier
    sock.bind((host, port))
    print(f"Starting Server on {host}, port: {port}")

    # allows for the server to recieve incoming client connections
    # arguement determines the max number of queued connections
    sock.listen(2)

    #accept() -- accept connection, returning new socket fd and client address
    connection, address = sock.accept()
    print(f"Connected to: {address}")

    while True:
        # Receive data from the client (up to 1024 bytes) and decode it
        data = connection.recv(1024).decode()

        # If no data is received, break the loop
        if not data:
            break
        print(f"RECIEVED from CLIENT: {data}")
        
        if data == "time":
            response = ("the time is 08:00")
        elif data == "latlong":
            response = ("Lat: latitude, Long: longitude")
        elif data == "RState":
            response = ("heres a return state... whatever that is")  
  
        else:
            response = "That is not a valid request"
            
        print(f'SENDING to CLIENT: {response}')
        connection.send(response.encode())
        
    # Close the client connection
    connection.close()

runServer()