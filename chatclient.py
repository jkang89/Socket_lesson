import socket
import sys
import select

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("localhost", 5555))

running = True
while running:
    inputready, outputready, exceptready = select.select([my_socket, sys.stdin], [], [])

    for s in inputready:
        if s == my_socket:
            data = s.recv(1024)
            print "%s" % data
        elif s == sys.stdin:
            user_input = s.readline()
            my_socket.sendall(user_input)
        else:
            print "Disconnected from server!"
            running = False

my_socket.close()