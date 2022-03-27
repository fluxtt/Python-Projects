# Python program to implement server side of chat room
import socket
import select
import sys

from _thread import *
from tracemalloc import start

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


# checks whether sufficient arguments have been provided
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

# takes the first argument from the command prompt as IP address
IP_address = str(sys.argv[1])

# takes the second argument from the command prompt as port number
Port = int(sys.argv[2])



#binds the server to an entered IP address and at the specified port number.
#The client must be aware of these parameters.
server.bind((IP_address, Port))

#listens for 10 active connections. This number can be increased as per convenience.
server.listen(10)

list_of_clients = []

def clientthread(conn, addr):

    # sends a message to the client whose user object is conn
    conn.send("Welcome to the chatroom!")
    while True:
        try:
            message = conn.recv(2048)
            if message:
                #prints the message and address of the user who just sent the message on the server terminal
                print("<" + addr[0] + "> " + message)

                # Calls broadcast function to send message to all
                message_to_send = "<" + addr[0] + "> " + message
                broadcast(message_to_send, conn)                
        
            else:
                #message may have no content if the connection is broken, in this case remove the connection
                remove(conn)
        
        except:
            continue

#broadcast message to all clients who's object is not the same as the one sending the message
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message)
            except:
                clients.close()
                
                #if link is broken, remove the client
                remove(clients)

#removes object from list of clients
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    #accepts connection request and stores conn, and addr
    conn, addr = server.accept()

    #maintains list of all clients for ease of broadcasting message to all
    list_of_clients.append(conn)

    # prints address of user that connects
    print(addr[0] + "connected")

    #creates individual thread for every user that connects
    start_new_thread(clientthread,(conn,addr))

conn.close()
server.close()