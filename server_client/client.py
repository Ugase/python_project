import socket

def start_client():
    host = '127.0.0.1'  # Localhost
    port = 12345        # Arbitrary non-privileged port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Connected to {host}:{port}")

        while True:
            command = input("Enter a command: ")
            s.sendall(command.encode('utf-8'))
            data = s.recv(1024)
            print(f"Received: {data.decode('utf-8')}")

if __name__ == "__main__":
    start_client()