import socket

INTERCEPTOR_PORT = 8800

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', INTERCEPTOR_PORT))
    
    print("PDCP Interceptor running...")
    
    while True:
        data, addr = sock.recvfrom(65535)
        print(f"Received PDCP packet of size {len(data)}")
        
        # Here you can process/modify the packet as needed
        
        # Forward the packet (you may need to modify this depending on your needs)
        # sock.sendto(data, (TARGET_IP, TARGET_PORT))

if __name__ == "__main__":
    main()