import socket

HOST = "localhost"
PORT = 1337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    loc = (HOST, PORT)
    server.bind(loc)
    server.listen(0)

    print(f"Created server sock {server}")

    while True:

        # For each client that will connect to the server
        # there will be a new socket
        client, addr = server.accept()
        print(f"Created client sock {client} with addr {addr}")

        with client:
            while True:
                msg = client.recv(1024)

                if not msg:
                    client.close()
                    break

                print(f"Received {msg} from {addr} at {client}")

                client.sendall(msg)
