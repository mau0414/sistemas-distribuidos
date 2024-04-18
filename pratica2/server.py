from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)

s.bind(('localhost', 3000))
s.listen()
(conn, addr) = s.accept()

start_time = time.time()
while True:

    # buffer de tamanho 1024
    data = conn.recv(1024)

    if not data: break

    conn.send(data)

end_time = time.time()
print('tempo de processamento no servidor', end_time-start_time)
conn.close()