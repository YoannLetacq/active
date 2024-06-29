import sys
from cli.cli_process import main_cli
from nmap.scan_tcp import scan_tcp
from nmap.scan_udp import scan_udp

# Hardcoded parameters
HARDCODED_HOST = 'localhost'
HARDCODED_PORT = 80


def main():
    if len(sys.argv) > 1:
        # Use the command line parameters if they exist (main_cli)
        main_cli()
    else:
        # Use the hardcoded parameters

        print("Using hardcoded parameters...")
        print(scan_tcp(HARDCODED_HOST, HARDCODED_PORT))
        print(scan_udp(HARDCODED_HOST, HARDCODED_PORT))


if __name__ == '__main__':
    main()
