# Explanation

This implementation is a single-threaded echo server. It works as follows:

- the server socket is created
- for each client that connected to the server:
  - the client socket is created
  - for each message that client has sent, send it back

# Example

## Server

### After running the server

`Created server sock <socket.socket fd=3, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337)>`

### After the client has connected and sent a message


```Created server sock <socket.socket fd=3, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337)>
Created client sock <socket.socket fd=4, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337), raddr=('127.0.0.1', 51216)> with addr ('127.0.0.1', 51216)
Received b'GET / HTTP/1.1\r\nHost: 127.0.0.1:1337\r\nUser-Agent: curl/8.0.1\r\nAccept: */*\r\n\r\n' from ('127.0.0.1', 51216) at <socket.socket fd=4, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337), raddr=('127.0.0.1', 51216)>```

## Client

### Connecting to the server via curl

`curl 127.0.0.1:1337 --http0.9`

### Getting the request back

```GET / HTTP/1.1
Host: 127.0.0.1:1337
User-Agent: curl/8.0.1
Accept: */*```
