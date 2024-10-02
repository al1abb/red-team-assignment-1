import socket

# TCP Scan
def scan_ports_tcp(host_port, start_port, end_port):
    print(f"\n===============Scanning TCP===============\n")
    print(f"Scanning ports on {host_port}...")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((host_port, port))

        if result == 0:
            print(f"(TCP) Port {port} is open")
        if result != 0:
            print(f"(TCP) Port {port} is closed")

        sock.close()

# UDP Scan
def scan_ports_udp(host_port, start_port, end_port):
    print(f"\n===============Scanning UDP===============\n")
    print(f"Scanning ports on {host_port}...")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)

        result = sock.sendto(b"Test", (host_port, port))

        if result == 0:
            print(f"(UDP) Port {port} is open")
        if result != 0:
            print(f"(UDP) Port {port} is closed")

        sock.close()

if __name__ == "__main__":
    target_hosts = input("Enter the host IP address: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    scan_ports_tcp(target_hosts, start_port, end_port)
    scan_ports_udp(target_hosts, start_port, end_port)