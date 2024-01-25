import socket
import multiprocessing

HOST = "localhost"
PORT = 1337


def client_thread(client, addr):
    with client:
        while True:
            msg = client.recv(1024)

            if not msg:
                client.close()
                break

            print(f"Received {msg} from {addr} at {client}")

            client.sendall(msg)


if __name__ == '__main__':
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

            # Start a new client thread for each client socket
            p = multiprocessing.Process(
                target=client_thread,
                args=(client, addr),
            )
            p.start()
            print(p)
