import socket
import threading

# Escaneja un port y mostra si esta obert. Recupera el banner.
def scan_port(target, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
            try:
                sock.sendall(b'Hello\r\n') # 
                banner = sock.recv(1024) # Llegeix 1024 bytes de resposta, si es reben es guarden al banner.
                if banner:
                    print(f"    Banner: {banner.decode().strip()}") ## Convertim els bytes a string i imprimim el contingut.
            except:
                pass

def main():
    target_ip = input("Enter target IP: ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))
    ports_to_scan = range(start_port, end_port + 1)

    threads = []

    print(f"\nScanning {target_ip} from port {start_port} to {end_port}...\n")

    for port in ports_to_scan:
        t = threading.Thread(target=scan_port, args=(target_ip, port))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("\nScan completed.")

if __name__ == "__main__":
    main()
