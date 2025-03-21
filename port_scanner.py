import socket

def scan_ports(target, ports):
    print(f"\n Scanning {target}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  #Timeout of 1 second per port
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f" Port {port} igit s OPEN")
        sock.close()

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    ports_to_scan = range(1, 1025)  #Scan the first 1024 ports
    scan_ports(target_ip, ports_to_scan)
