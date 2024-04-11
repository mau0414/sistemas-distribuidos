import zmq

def main():

    try:
        context = zmq.Context()
        # amarra um socket chamado frontend para conexoes na porta 5559
        frontend = context.socket(zmq.XREP)
        frontend.bind("tcp://*:5559")
        # amarra um socket chamado backend para conexoes na porta 5560
        backend = context.socket(zmq.XREQ)
        backend.bind("tcp://*:5560")

        zmq.device(zmq.QUEUE, frontend, backend)
    except(Exception):
        print("bringing down zmq device")
    finally:
        pass
        frontend.close()
        backend.close()
        context.term()

if __name__ == "__main__":
    main()
