import time
import zmq

# porta do backend
port = '5560'
context = zmq.Context()
# define socket como socket de resposta (server)
socket = context.socket(zmq.REP)
# liga socket a um endereco - o tcp serve apenas para indicar que se deseja usar protocolo tcp
socket.connect("tcp://localhost:%s" % port)

while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f"Received request from client: {message}")

    request_number = (message.split(b' ')[3]).decode()
    client_number = (message.split(b' ')[6]).decode()

    response_msg = 'resposta do servidor para requisicao %s do cliente %s' % (request_number, client_number)

    #  Send reply back to clientb'%d' % (random_number)
    socket.send(response_msg.encode())