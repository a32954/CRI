import socket

def run_server():
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ## socket.AF_INET -> especifica que é IPv4
    ## socket.SOCK_STREAM -> especifica que e o protocolo TCP

    server_IP="172.16.32.168"
    port = 1889631
    ## Local host, colocar um IP caso saiba que o mesmo é estatico    
    ## port ->  porta que vai ser usada, utilizar uma acima de 1023

    server.bind("172.16.32.168","1889631")

    server.listen(0)
    print(f"Listening on {server_IP}:{port}")

    client_socket,client_address = server.accept()
    print(f"Accepted	connection	from	{client_address[0]}:{client_address[1]}")

    


