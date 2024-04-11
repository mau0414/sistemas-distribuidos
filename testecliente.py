import random
import threading
import zmq
import time

# numero de clientes
num_threads = 50
num_requisicoes_p_cliente = 1000

# inicializacao de um cliente
def client_service(client_number):
    context = zmq.Context()

    # cria e define socket de requisicao (cliente)
    socket = context.socket(zmq.REQ)

    # conecta ao frontend
    socket.connect("tcp://localhost:5559")

    # realiza 4 requisicoes
    for request in range(num_requisicoes_p_cliente):
        request_msg = b'requisicao de numero %d do cliente %d' % (request, client_number)
        print('sending request %d from cliente %d to server' %(request, client_number))
        # envia requisicao
        socket.send(request_msg)

        #  recebe resposta
        message = socket.recv()
        print(f"Received reply: [ {message} ]")

# lista de threads
threads = []

# cria e inicia as threads
for i in range(num_threads):
    thread = threading.Thread(target=client_service, args=(i,))
    threads.append(thread)
    start_time = time.time()
    thread.start()

# aguarda termino de todas as threads
for thread in threads:
    thread.join()

end_time = time.time()
total_time = end_time - start_time
print('total de requisicoes:', num_threads * num_requisicoes_p_cliente)
print('tempo de resposta:', total_time)

