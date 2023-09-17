import socket
import logging
import threading
from json import load
import status_code

CONFIGS = load(open("config.json"))

logging.basicConfig(level=logging.INFO,
                    format="[%(levelname)s] - [%(asctime)s] - [%(filename)s] - %(message)s",
                    filename="log.log",
                    filemode="a",
                    encoding="utf-8")


def client_while(client_socket: socket.socket):
	pass


def main():
	# 创建套接字
	SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	SERVER_SOCKET.bind((CONFIGS["HOST"], CONFIGS["PORT"]))
	SERVER_SOCKET.listen()
	
	# 等待用户连接
	while True:
		# 用户连接，启动新线程处理
		client_socket, client_addr = SERVER_SOCKET.accept()
		
		client_thread = threading.Thread(target=client_while, args=(client_socket,))
		
		


if __name__ == '__main__':
	logging.info("服务端运行")
	
	try:
		main()
	except KeyboardInterrupt:
		logging.debug("Ctrl+C输入")
		
	# finally:
	# 	logging.info("服务端退出")
	# 	exit(0)
