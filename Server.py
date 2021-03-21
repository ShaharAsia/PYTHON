import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "out"
# declare my address (server address)
PORT = 5050  # choose a port
IP = socket.gethostbyname(socket.gethostname())  # get IP
ADDR = (IP, PORT)

# create a socket() and bind it into ADDR , Params:
#        1. Address Family - AF_INET for IPv4L, AF_UNIX for unix domain ..
#        2. Socket type - SOCK_STREAM is standard for streaming data into the socket ..
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"New Client is being handled - {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if (msg_length):
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if (msg == DISCONNECT_MSG):
                connected = False
            print(f"Messege: [{addr}] {msg}")
    conn.close()


def start():
    print("[Listening]...")
    server.listen()  # listen for new clients
    while True:
        # when new client accepted - store his addr and connection to communicate back with him:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[Active Connections] {threading.active_count() - 1}")


print("[Starting]...")
start()