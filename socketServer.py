import socket

def handle_request(client_socket):
    # Receive data from the client
    request = client_socket.recv(1024).decode('utf-8')
    
    # Process the request and generate a response
    response = 'Hello, client!'
    
    # Send the response back to the client
    client_socket.send(response.encode('utf-8'))
    
    # Close the connection
    client_socket.close()

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a specific address and port
    server_socket.bind(('localhost', 9090))
    
    # Start listening for incoming connections
    server_socket.listen(1)
    
    print('Server is listening on port 9090...')
    
    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print('Received connection from:', client_address)
        
        # Handle the client request in a separate thread or process
        handle_request(client_socket)

start_server()
