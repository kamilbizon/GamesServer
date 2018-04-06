import json


class OnlineMessage:
    def __init__(self):
        self._hdr = ''
        self._body = ''

    def set_header(self, new_header):
        self._hdr += new_header

    def set_body(self, new_body):
        self._body += new_body

    def encode(self):
        encoded_message = []
        encoded_message.append(self._hdr)
        encoded_message.append(self._body)
        return bytes(json.dumps(encoded_message), 'utf-8')

    def decode(self, message_received):
        message_received = message_received.decode('utf-8')
        message_received = json.loads(message_received)
        self._hdr = message_received[0]
        self._body = message_received[1]
        return self
