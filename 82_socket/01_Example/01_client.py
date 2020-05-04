import socket
# Create the client side socket.
c = socket.socket()
# we have IP address and working with IPV4/IPV6
# The second one is IP Address.
# The bind the socket to port numnber is server job.
# The client is simply to conenc the socket.
# Client have to give two parameters:
# 1. IP address: Server IP address is 'localhost'
# 2. Port number: server port number is 9999
c.connect (('localhost', 9999))
