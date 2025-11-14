import socket

def run_client():
    
    client	= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip	= "10.58.55.133"		
    server_port	= 5005
    client.connect((server_ip, server_port))

    while True:
	
        #	input	message	and	send	it	to	the	server	
        msg	= input("Enter	message:")
	    
        client.send(msg.encode("utf-8")[:1024])

        response = client.recv(1024)

        response = response.decode("utf-8")

        if response.lower() == "closed":

            break

        print (f"Recieved: {response}")

        client.close()

        print ("connection to server closed.")
        
run_client()