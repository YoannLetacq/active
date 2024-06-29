import socket
from nmap.get_service import get_service


def scan_udp(host, port):

    try:
        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)

        # Send an empty packet to the target
        sock.sendto(b'', (host, port))

        # Wait for a response
        res = sock.recvfrom(1024)

        if res:
            sock.close()
            service = get_service(port)
            return f"Port {port} is open, Service: {service}"
        else:
            return f"Port {port} is closed"

    except socket.error as e:

        return f"Cannot connect to {host}:{port}, error: {e}"
