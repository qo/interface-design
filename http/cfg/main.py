import socket
import select
import multiprocessing
import os
import datetime

HOST = "localhost"
PORT = 1337

N_OF_THREADS = 1


def getResponse(code):
    tmpl = ""
    if code == 200:
        tmpl = "HTTP/1.0 200 OK\nDate: {date}\nContent-Type: text/html\n"
    else:
        tmpl = "HTTP/1.0 404 Not Found\nDate: {date}\nContent-Type: text/html\n"
    return tmpl.format(date = datetime.datetime.now())


def socket_thread(server):
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

                if not (r in data):
                    data[r] = ""

                data[r] += r.recv(1024).decode()

                if len(data[r]) == 0:
                    rlist.remove(r)
                    print(f"Client disconnected {client}")
                    r.close()

                else:
                    if "\r\n" in data[r]:

                        request = data[r].split()

                        if request[0] == "GET":
                            filename = request[1][1:]
                            path = os.path.join("..", "assets", filename)
                            try:
                                file = open(path)
                                data[r] = (getResponse(200) + file.read()).encode()
                            except:
                                data[r] = (getResponse(404) + "Error").encode()
                            print(data[r])
                            rlist.remove(r)
                            wlist.append(r)

        for w in writes:

            w.send(data[w])
            print(f"Data sent {data[w]} to {w}")

            del data[w]

            wlist.remove(w)
            rlist.append(w)


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        loc = (HOST, PORT)
        server.bind(loc)
        server.listen(0)

        print(f"Created server sock {server}")

        # Start 4 threads
        for _ in range(N_OF_THREADS):
            p = multiprocessing.Process(
                target=socket_thread,
                args=[server],
            )
            p.start()
            print(p)
