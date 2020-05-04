import socket

# We have to pass two parameters:
# 1. Type of network: IPV4/IPV6or or none for IPV4.
# 2. Type of protocol: TCP/or UDP or none for TCP.
s = socket.socket()
print ('Socket created')

# we are makeing this socket as the server socket.
# We have socket that accepts the connection. 
# We weed the IP address and Port number.
# We bind a socket with port number.
# we have to pass two parameters:
# 1. IP address for server.
#    Right now we use the same machine for client and server.
#    Server is 'localhost'
# 2. Port Number: 9999 (port number which no one used fro 0 to 65535)
#    DO not use the port number < 1000. They are used in other services.
s.bind(('localhost', 9999))

# Once you bind the socket to IP address and port number.
# We start listening to the client. Wating for the clients (1-n clients) to connect.
# we want 3 clients to connect.
s.listen(3)
print('Waiting for connections')

# Now, we need to process the connection in a loop.
while True:
    # we got client socket and address from the client.
    c, addr = s.accept()
    # Once we accept the data, we have to send to the client
    name = c.recv(1024).decode()
    print ("Connected with:", addr, " name:", name)
    # We want to send something to Client
    # c.send ("Welcome to Peter's Computer")
    # Server need to send the byte format.
    c.send(bytes ("Welcome to Peter's Computer", "utf-8"))
    # Once the job is done. Close the connection.
    c.close()
