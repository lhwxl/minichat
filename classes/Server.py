import socket
from classes.Singleton import Singleton


@Singleton
class Server:
	def __init__(self, addr=("", 8888)):
		self.SERVER_SOCKET = socket.socket(addr)
