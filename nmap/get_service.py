import socket


def get_service(port):
    try:
        return socket.getservbyport(port)
    except OSError:
        return 'Unknown service'
