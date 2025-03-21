import socket

def scan_ports(target, ports):
    print(f"\nScanning {target}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout of 1 second per port
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        elif result == 111:
            print(f"Port {port} is CLOSED (Connection Refused)")
        elif result == 110:
            print(f"Port {port} is CLOSED (Timeout)")
        else:
            print(f"Port {port} status unknown, result code: {result}")
        sock.close()

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    ports_to_scan = [22, 80, 443]  # Ports to scan
    scan_ports(target_ip, ports_to_scan)
