import socket
from sys import platform
import http.server
import socketserver
import pyqrcode


def get_my_ip():
    '''
    Create a socket to a "fake" IP address, then read socket sender address.
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.2.3.4", 80))
    return s.getsockname()[0]


def start_server(port):
    '''
    Start HTTP server serving the current directory.
    '''
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nThanks for using me!')


PORT = 8080


def main():
    ip_addr = get_my_ip()
    server_url = ' http://{}:{} '.format(ip_addr, PORT)
    print('Serving at following URL:')
    print('#'*len(server_url))
    print(server_url)
    print('#'*len(server_url))
    print('Use {}-C to stop.'.format('CMD' if platform == 'darwin' else 'CTRL'))

    qrcode = pyqrcode.create(server_url)
    print(qrcode.terminal(quiet_zone=1))
    start_server(PORT)


if __name__ == '__main__':
    main()
