import socket
import select

HOST = 'localhost'
PORT = 1337

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        loc = (HOST, PORT)
        server.bind(loc)
        server.listen(0)

        print(f"Created server sock {server}")

        # Dictionary with read/wrote messages
        data = {}

        # Read/write socket (file descriptors) lists
        rlist = []
        wlist = []

        # Append server socket to read list on start
        rlist.append(server)

        while True:

            reads, writes, _ = select.select(rlist, wlist, [], 0)

            for r in reads:

                if r == server:
                    # For each client that will connect to the server
                    # there will be a new socket
                    client, addr = server.accept()
                    print(f"Created client sock {client} with addr {addr}")

                    # Append client socket to read list
                    rlist.append(client)

                else:
                    # Receive message from client
                    # and remove it from reading list
                    msg = r.recv(1024)
                    rlist.remove(r)

                    data[r] = msg

                    if len(data[r]) != 0:
                        wlist.append(r)
                    else:
                        print(f"Client disconnected {r}")
                        r.close()

            for w in writes:

                send = w.send(data[w])
                print(f"Data sent {data[w]} to {w}")

                del data[w]

                wlist.remove(w)
                rlist.append(w)
