### TCPSocketServer
> simple python TCPSocketServer opens port 9090

## Start server
```
> python3 socketServer.py

Server is listening on port 9090...
Received connection from: ('127.0.0.1', 12345)
Received connection from: ('127.0.0.1', 54321)
```

## Connect using telnet or netcat
###  telnet 
```
> telnet localhost 9090

Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
> hi
Hello, client!Connection closed by foreign host.
```


### netcat
```
> nc localhost 9090
> hi from nc
 Hello, client!
```
