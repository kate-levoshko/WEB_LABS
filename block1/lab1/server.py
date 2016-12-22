import socket, select, sys, queue, json
import parse
from queue import Queue


def input_serv_port():
    print('Please, enter the port >>>')
    data = input()
    if data == "exit":
        return
    return data

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(0)

while True:
    try:
        TCP_PORT = int(input_serv_port())
        sock.bind(("", TCP_PORT))
        break
    except:
        print("error input")

sock.listen(10)
inputs = [ sock ]
outputs = [ ]

message_queues = {}

def getInfo():
    addr_list = []
    for s in inputs:
        if s != sock:
            addr_list.append(s.getpeername())
    return json.dumps(addr_list)

def getAmount():
   return '10'

def mainf():
    while True:
        readable, writable, exceptional = select.select(inputs, outputs, inputs, 0.05)

        for client in readable:
            if client is sock:
                connection, client_address = client.accept()
                connection.setblocking(0)
                inputs.append(connection)

                message_queues[connection] = Queue()
            else:
                data = client.recv(5000)
                if data:
                    print("<<<", data.decode("utf-8"))
                    message_queues[client].put(data)
                    if client not in outputs:
                        outputs.append(client)
                else:
                    if client in outputs:
                        outputs.remove(client)
                    inputs.remove(client)
                    client.close()
                    del message_queues[client]

        for client in writable:
            if dict.__len__(message_queues) > 0:
                if message_queues.get(client):
                    try:
                        next_msg = message_queues[client].get_nowait()
                    except queue.Empty:
                        outputs.remove(client)
                    else:
                        if next_msg.decode('utf-8') == "info":
                            client.send(getInfo().encode('utf-8'))
                            print(getInfo().encode('utf-8'))
                        elif next_msg.decode('utf-8') == "amount":
                            client.send(getAmount().encode('utf-8'))
                            print(getAmount())
                        else:
                            client.send(parse.getJson(next_msg.decode('utf-8')).encode('utf-8'))

        for client in exceptional:
            inputs.remove(client)
            if client in outputs:
                outputs.remove(client)
            client.close()
            del message_queues[client]
			
mainf();
