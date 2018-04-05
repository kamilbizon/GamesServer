import socket
import json

class Client:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    message = [1, 2, 3]
    s.connect(('127.0.0.1', 5005))
    s.send(bytes(json.dumps(message), 'ascii'))
    s.settimeout(5)
    data = None
    try:
        while True:
            data = s.recv(512)
            print(data)
    except:
        pass