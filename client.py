import socket
import struct

import cv2
import numpy as np

from base import Input


class Client(Input):
	def __init__(self, local_port=5555, server_port=1920, packet_size=60000):
		super().__init__()
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.socket.bind(('', local_port))
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, packet_size+16)
		self.size = packet_size
		self.port = server_port
		self.address = socket.gethostbyname('roborio-192-frc.local')
		self.socket.sendto('join'.encode(), (self.address, server_port))

	def get(self):
		ar = self.socket.recv(self.size)
		ar = np.fromstring(ar)
		ar = cv2.imdecode(ar, cv2.IMREAD_COLOR)
		return ar

	def send(self, data):
		print(data)
		if data is None:
			return
		send = struct.pack('>{}d'.format(len(data)), *data)
		self.socket.sendto(send, (self.address, self.port))
