import socket

class Instrument(object):
    "VXI-11 instrument interface client"
    def __init__(self, host, port=9999):
        "Create new VXI-11 instrument object"
        self.host = host
        self.port = port

    def write_raw(self, data):
        "Write binary data to instrument"
        # Create a socket (SOCK_STREAM means a TCP socket)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        try:
            # Connect to server and send data
            sock.connect((self.host, self.port))
            sock.sendall(data + "\n")
        finally:
            sock.close()

    def ask_raw(self, data):
        "Write then read binary data"
        # Create a socket (SOCK_STREAM means a TCP socket)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        try:
            # Connect to server and send data
            sock.connect((self.host, self.port))
            sock.sendall(data + "\n")
            # Receive data from the server and shut down
            received = sock.recv(16)
            received = sock.recv(int(received), socket.MSG_WAITALL)
        finally:
            sock.close()
        return received

    def write(self, message, encoding = 'utf-8'):
        "Write string to instrument"
        self.write_raw(str(message).encode(encoding))

    def ask(self, message, encoding = 'utf-8'):
        "Write then read string"
        return self.ask_raw(str(message).encode(encoding)).decode(encoding).rstrip('\r\n')
