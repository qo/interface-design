# Explanation

This implementation is a HTTP 1.0 server. It works as follows:

- the request is parsed
- the last part of the request is interpreted as a filename
- the file with the specified filename is opened in ../assets directory

# Example

## Server

### After running the server

```
Created server sock <socket.socket fd=3, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337)>
<Process name='Process-1' pid=39014 parent=39013 started>
<Process name='Process-2' pid=39015 parent=39013 started>
<Process name='Process-3' pid=39016 parent=39013 started>
<Process name='Process-4' pid=39017 parent=39013 started>
```

### After the client 1 has connected and sent a message

```
Created client sock <socket.socket fd=9, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337), raddr=('127.0.0.1', 55662)> with addr ('127.0.0.1', 55662)
Data sent b'<!DOCTYPE html>\n<html>\n  <body>\n    Hello, World!\n  </body>\n</html>\n' to <socket.socket fd=9, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337), raddr=('127.0.0.1', 55662)>
```

### After the client 2 has connected and sent a message

```
Created client sock <socket.socket fd=11, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337), raddr=('127.0.0.1', 41676)> with addr ('127.0.0.1', 41676)
Data sent b'<!DOCTYPE html>\n<html>\n  <body>\n    Hello, World!\n  </body>\n</html>\n' to <socket.socket fd=11, family=2, type=1, proto=0, laddr=('127.0.0.1', 1337), raddr=('127.0.0.1', 41676)>
```

## Client 1

### Connecting to the server via curl

`curl 127.0.0.1:1337 --http0.9`

### Getting the request back

```
GET / HTTP/1.0
Host: 127.0.0.1:1337
User-Agent: curl/8.0.1
Accept: */*
```

## Client 2

Same as client 1.
