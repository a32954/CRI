import socket

def run_server():
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ## socket.AF_INET -> especifica que é IPv4
    ## socket.SOCK_STREAM -> especifica que e o protocolo TCP

    server_IP="127.0.0.1"
    port = 1889631
    ## Local host, colocar um IP caso saiba que o mesmo é estatico    
    ## port ->  porta que vai ser usada, utilizar uma acima de 1023

