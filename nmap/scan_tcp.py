import socket
from nmap.get_service import get_service


def scan_tcp(host, port):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a connection timeout
        sock.settimeout(1)

        # Try to connect to the target
        err = sock.connect_ex((host, port))

        sock.close()

        if err == 0:
            service = get_service(port)
            return f'{host}:{port} - {service} is open'
        else:
            return f'{host}:{port} is closed'

    except socket.error:
        return f'Cannot connect to {host}:{port}'

