import argparse
from nmap.scan_tcp import scan_tcp
from nmap.scan_udp import scan_udp


def main_cli():
    parser = argparse.ArgumentParser(description='Simple port scanner')
    parser.add_argument('host', help='Target host')
    parser.add_argument('-p', '--ports', type=str, help='Port or range of ports to scan (format: PORT or START-END)')
    parser.add_argument('-u', '--udp', action='store_true', help='Perform UDP scan')
    parser.add_argument('-t', '--tcp', action='store_true', help='Perform TCP scan')
    args = parser.parse_args()

    if args.ports:
        if '-' in args.ports:
            try:
                start_port, end_port = map(int, args.ports.split('-'))
                for port in range(start_port, end_port + 1):
                    if args.udp:
                        print(scan_udp(args.host, port))
                    else:
                        print(scan_tcp(args.host, port))
            except ValueError:
                parser.error("Invalid format for --ports. Use START-END (e.g., 80-90).")
        else:
            try:
                port = int(args.ports)
                if args.udp:
                    print(scan_udp(args.host, port))
                else:
                    print(scan_tcp(args.host, port))
            except ValueError:
                parser.error("Invalid format for --ports. Use a single port (e.g., 80) or START-END (e.g., 80-90).")
    else:
        parser.error("You must specify a port or a range of ports.")


if __name__ == '__main__':
    main_cli()
