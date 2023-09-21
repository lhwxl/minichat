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
	pass
		
		


if __name__ == '__main__':
	logging.info("服务端运行")
	
	try:
		main()
	except KeyboardInterrupt:
		logging.debug("Ctrl+C输入")
		
	# finally:
	# 	logging.info("服务端退出")
	# 	exit(0)
