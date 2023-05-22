import socket
import base64


class custum_socket:
   my_socket = socket.socket()

   def __init__(self):
       pass

   def sendto(self, message, remote_socket):
       message_bytes = message.encode('ascii')
       base64_bytes = base64.b64encode(message_bytes)
       self.my_socket.connect(remote_socket)
       self.my_socket.send(base64_bytes)

   def recvfrom(self, buffer_size):
       self.my_socket.bind(("0.0.0.0", 12345))
       self.my_socket.listen(2)
       conn, address = self.my_socket.accept()
       base64_bytes = conn.recv(buffer_size)
       message_bytes = base64.b64decode(base64_bytes)
       message = message_bytes.decode('ascii')
       return message
   
c=custum_socket()
c.sendto("Hello", ("127.0.0.1", 12345))