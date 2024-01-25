# Multithreading with Go's coroutines (goroutines) and WaitGroups
mt:
	go run ./multithreading/main.go

# Linux pipe implementation with processes and standard i/o
ppr:
	go run ./piper/main.go

# Single-threaded non-multiplexed echo server implementation
echo-st:
	python ./echo/st/main.py

# Milti-threaded non-multiplexed echo server implementation
echo-mt:
	python ./echo/mt/main.py

# Single-threaded multiplexed echo server implementation
echo-stmx:
	python ./echo/stmx/main.py

# Multi-threaded multiplexed echo server implementation
echo-mtmx:
	python ./echo/mtmx/main.py

# All the http-* servers are based on echo echo-mtmx

# HTTP 0.9 server implementation
http-0.9:
	python ./http/0.9/main.py

# HTTP 1.0 server implementation
http-1.0:
	python ./http/1.0/main.py

# Configurable HTTP 1.0 server implementation
http-cfg:
	python ./http/cfg/main.py
