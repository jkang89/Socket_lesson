import socket
import sys
import select

def format_message(message):
    if "::" in message:
        message = message.split("::", 1)
        new_message = "[%s] %s" % (message[0], message[1])
        return new_message
    else:
        return message

def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(("localhost", 5555))
    
    running = True
    while running:
        inputready, outputready, exceptready = select.select([my_socket, sys.stdin], [], [])

        for s in inputready:
            if s == my_socket:
                data = s.recv(1024)
                print format_message(data)
            elif s == sys.stdin:
                user_input = s.readline()
                if user_input == "/quit\n":
                    print "Logged out."
                    running = False
                else:
                    my_socket.sendall(user_input)
            else:
                print "Disconnected from server!"
                running = False

    my_socket.close()

main()