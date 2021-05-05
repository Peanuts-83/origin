#! /usr/bin/python3
"""
The socketserver module simplifies the task of writing network servers.
There are four basic concrete server classes from BaseServer:
class socketserver.TCPServer >> UnixStreamServer
                             >> UDPServer >> UnixDatagramServer
                             
To build asynchronous handlers, use the ThreadingMixIn and ForkingMixIn classes.
"""
import socket, socketserver, threading

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        # self.request = TCP socket connected to the client
        data = str(self.request.recv(1024), 'utf-8')
        cur_thread = threading.current_thread()
        response = bytes(f'{cur_thread}:{data}', 'utf-8')
        self.request.sendall(response)
        
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def client(ip, port, msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(msg, 'utf-8'))
        response = str(sock.recv(1024), 'utf-8')
        print(f'Received: {response}')
        
if __name__ == '__main__':
    # 0 for arbitrairy choose free port
    HOST, PORT = 'localhost', 0
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    with server:
        ip, port = server.server_address

        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread:", server_thread.name)

        client(ip, port, "Hello World 1")
        client(ip, port, "Hello World 2")
        client(ip, port, "Hello World 3")

        server.shutdown()