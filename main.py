import socket
import logging
import logging.handlers
import threading

from json import load
from sys import exit

import status_code

log = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s %(levelname)s [%(filename)s]: %(message)s')
log.setLevel(logging.DEBUG)

file_handler = logging.handlers.TimedRotatingFileHandler(filename=f"./log.log", encoding="utf-8", when="D")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

log.addHandler(file_handler)
log.addHandler(stream_handler)

CONFIGS = load(open("config.json"))
log.debug("Config loaded")


def client_while():
	pass


def main():
	pass




if __name__ == '__main__':
	log.info("Server running")

	try:
		main()
	except KeyboardInterrupt:
		log.debug("Ctrl+C inputted,exitting")
	except Exception as e:
		log.error(f"\nUnknown error,error massage: \n{e}")
	finally:
		logging.info("服务端退出")
		exit(0)
