# Multithreading with Go's coroutines (goroutines) and WaitGroups
mt:
	go run ./multithreading/main.go

# Linux pipe implementation with processes and standard i/o
ppr:
	go run ./piper/main.go

# Single-threaded non-multiplexed echoserver implementation
echo-st:
	python ./echo/st/main.py

# Milti-threaded non-multiplexed echoserver implementation
echo-mt:
	python ./echo/mt/main.py
