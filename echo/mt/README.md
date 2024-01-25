# Explanation

This implementation is a multi-threaded echo server. It works as follows:

- the server socket is created
- for each client that connected to the server:
  - a new thread is created and in this thread:
    - the client socket is created
    - for each message that client has sent, send it back

# Example

## Server

### After running the server

```
Created server sock <socket.socket fd=3, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337)>
```

### After the client 1 has connected and sent a message

```
Created client sock <socket.socket fd=4, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337), raddr=('127.0.0.1', 55712)> with addr ('127.0.0.1', 55712)
<Process name='Process-1' pid=15271 parent=15268 started>
Received b'GET / HTTP/1.1\r\nHost: 127.0.0.1:1337\r\nUser-Agent: curl/8.0.1\r\nAccept: */*\r\n\r\n' from ('127.0.0.1', 55712) at <socket.socket fd=4, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337), raddr=('127.0.0.1', 55712)>
```

### After the client 2 has connected and sent a message

```
Created client sock <socket.socket fd=6, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337), raddr=('127.0.0.1', 49750)> with addr ('127.0.0.1', 49750)
<Process name='Process-2' pid=15306 parent=15268 started>
Received b'GET / HTTP/1.1\r\nHost: 127.0.0.1:1337\r\nUser-Agent: curl/8.0.1\r\nAccept: */*\r\n\r\n' from ('127.0.0.1', 49750) at <socket.socket fd=6, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337), raddr=('127.0.0.1', 49750)>
```

## Client 1

### Connecting to the server via curl

`curl 127.0.0.1:1337 --http0.9`

### Getting the request back

```
GET / HTTP/1.1
Host: 127.0.0.1:1337
User-Agent: curl/8.0.1
Accept: */*
```

## Client 2

Same as client 1.
