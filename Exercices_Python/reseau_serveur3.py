#! /usr/bin/python3
"""
The socketserver module simplifies the task of writing network servers.
There are four basic concrete server classes from BaseServer:
class socketserver.TCPServer >> UnixStreamServer
                             >> UDPServer >> UnixDatagramServer
"""
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        # self.request = TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address))
        print(self.data)
        # return same string upper()
        self.request.sendall(self.data.upper())
        
if __name__ == '__main__':
    HOST, PORT = 'localhost', 12802
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
        
# ONLY 1 thread for each connexion!