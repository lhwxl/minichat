import socket
import logging
import logging.handlers
import threading

from json import load
from sys import exit

import status_code

# 定义日志记录器和日志格式
log = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s %(levelname)s [%(filename)s]: %(message)s')
log.setLevel(logging.DEBUG)

# 将日志输出到文本
# 等级为debug
file_handler = logging.handlers.TimedRotatingFileHandler(filename=f"./debugLogs/debugLog.log", encoding="utf-8", when="D")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

# 将日志输出到文本
# 等级为info
debug_file_handler = logging.handlers.TimedRotatingFileHandler(filename=f"./logs/Log.log", encoding="utf-8", when="D")
debug_file_handler.setFormatter(formatter)
debug_file_handler.setLevel(logging.INFO)

# 将日志输出到屏幕
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

# 将日志处理器添加到记录器
log.addHandler(file_handler)
log.addHandler(debug_file_handler)
log.addHandler(stream_handler)

CONFIGS = load(open("config.json"))


def client_while():
	pass


def main():
	while True:
		pass


if __name__ == '__main__':
	log.info("Server running")

	try:
		main()

	# Ctrl+C 退出
	except KeyboardInterrupt:
		log.debug("Ctrl+C inputted")

	# 未捕获的异常将输出
	except Exception as e:
		log.error(f"\nUnknown error,error massage: \n{e}")
	finally:
		log.info("exiting")
		exit(0)
