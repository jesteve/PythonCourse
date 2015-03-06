import SocketServer
from lecroy_emulator import emulate



class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.query = self.request.recv(1024).strip()
        print "{0} wrote : {1}".format(self.client_address[0], self.query)
        # Generate the response and send it
        response = emulate(self.query)
        self.request.sendall('{0:016d}{1}'.format(len(response),response))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
