# Explanation

This implementation is a single-threaded multiplexed echo server. It works as follows:

- the server socket is created
- N_OF_THREADS threads created for working with sockets
- each thread does the following:
  - the server socket is appended to the list of readers
  - for each reader that is a server:
    - the client socket is created
    - the client socket is appended to the list of readers
  - for each reader that is a client:
    - the message sent by the client is saved and marked as his message
    - the client socket is removed from the list of readers
    - the client socket is appended to the the list of writers
  - for each writer:
    - the message is sent but this writer is sent back

# Example

## Server

### After running the server

```
Created server sock <socket.socket fd=3, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337)>
<Process name='Process-1' pid=27288 parent=27287 started>
<Process name='Process-2' pid=27289 parent=27287 started>
<Process name='Process-3' pid=27290 parent=27287 started>
<Process name='Process-4' pid=27291 parent=27287 started>
```

### After the client 1 has connected and sent a message

```
Created client sock <socket.socket fd=11, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337), raddr=('127.0.0.1', 54778)> with addr ('127.0.0.1', 54778)
Data sent b'GET / HTTP/1.1\r\nHost: 127.0.0.1:1337\r\nUser-Agent: curl/8.0.1\r\nAccept: */*\r\n\r\n' to <socket.socket fd=11, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337), raddr=('127.0.0.1', 54778)>
```

### After the client 2 has connected and sent a message

```
Created client sock <socket.socket fd=12, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337), raddr=('127.0.0.1', 54794)> with addr ('127.0.0.1', 54794)
Data sent b'GET / HTTP/1.1\r\nHost: 127.0.0.1:1337\r\nUser-Agent: curl/8.0.1\r\nAccept: */*\r\n\r\n' to <socket.socket fd=12, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337), raddr=('127.0.0.1', 54794)>
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
