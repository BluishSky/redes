# MakeUpperCaseClientUsingUDP   
  

from socket import *

# STUDENTS - replace with your server machine's name 
serverName = "localhost" #ou 127.0.0.1

# STUDENTS - randomize your port number (use the same one in the server)         
# This port number in practice is often a "Well Known Number"  
serverPort = 12000

# create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)


# get user's input from keyboard
message = input("Input lowercase sentence: ")

# send user's sentence out socket; destination host and port number req'd
# need to cast message to bytes for Python 3  
clientSocket.sendto(message.encode(), (serverName, serverPort))


print ("Sent to Make Upper Case Server running over UDP: ", message)

# receive modified sentence in all upper case letters from server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# output modified sentence and close the socket
print ("Received back from Server: ", modifiedMessage.decode())

# close the UDP socket
clientSocket.close()