from socket import *
import time
import threading

HOST = 'localhost'
PORT = 3000
num_threads = 10
num_requisicoes_p_cliente = 10
threads = []


def client_service():

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))

    for i in range(100000):
        s.send(b'hello world')
        data = s.recv(1024)
        print(data)

    s.close()

# cria e inicia as threads
for i in range(num_threads):
    thread = threading.Thread(target=client_service)
    threads.append(thread)
    start_time = time.time()
    thread.start()


# aguarda termino de todas as threads
for thread in threads:
    thread.join()

end_time = time.time()

print('tempo de processamento:', end_time-start_time)