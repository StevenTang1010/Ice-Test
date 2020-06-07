# --------------------------------------
# Name:        log.py
# Date:        2020-03-25
# Author:      Steven_Tang
# Description: 日志输出模块
# --------------------------------------

import os
from pathlib import Path

from loguru import logger

log_name = Path(os.path.dirname(os.path.abspath(__file__)), 'excute', 'runtime_{time}.log')

logger.add(log_name, rotation='100 MB', retention='7 days', enqueue=True)

'''
日志，用于打印执行及错误日志
'''


# def __init__(self):
# 	self.e_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'excute')
# 	self.time_now = time.strftime('%m%d%H%M', time.localtime(time.time()))
# 	self.elog_name = os.path.join(self.e_path, self.time_now + '.log')
# 	if os.path.exists(os.path.dirname(self.elog_name)):
# 		pass
# 	else:
# 		os.mkdir(os.path.dirname(self.elog_name))
# 	self.logger = logging.getLogger(__name__)
# 	log_handle = logging.FileHandler(self.elog_name, mode='a')
# 	self.logger.setLevel(level=logging.DEBUG)
# 	format = logging.Formatter(fmt="%(asctime)s %(filename)s[line:%(lineno)d] <%(levelname)s> %(message)s")
# 	log_handle.setFormatter(format)
# 	self.logger.addHandler(log_handle)

def info(msg):
	'''打印 info 级别的日志'''
	logger.info(msg)


def debug(msg):
	'''打印debug 级别的日志'''
	logger.debug(msg)


def warning(msg):
	'''打印 warning 级别的日志'''
	logger.warning(msg)


def error(msg):
	'''打印 error 级别的日志'''
	logger.error(msg)


# log = Log()

if __name__ == '__main__':
	print(log_name)
	pass
# e = []
