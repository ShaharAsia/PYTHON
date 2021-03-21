import socket

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "out"
SERVER = socket.gethostbyname(socket.gethostname())  # get IP
PORT = 5050  # choose a port
ADDR = (SERVER, PORT)

#  generate client socket:
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(msg)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


send("HEY1")
send("HEY2")
send("HEY3")
send("HEY4")