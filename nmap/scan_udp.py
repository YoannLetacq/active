import socket
from nmap.get_service import get_service


def scan_udp(host, port):

    try:
        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(5)

        # Send an empty packet to the target
        sock.sendto(b'', (host, port))

        try:
            # Wait for a response
            _data, _addr = sock.recvfrom(1024)

            sock.close()
            service = get_service(port)
            return f"Port {port} is open, Service: {service}"
        except socket.timeout:
            sock.close()
            return f"Port {port} is closed"
    except socket.error as e:
        return f"Cannot connect to {host}:{port}, error: {e}"
