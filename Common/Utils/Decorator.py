# --------------------------------------
# Name:        Decorator.py
# Date:        2020-03-25
# Author:
# Description: 装饰器模块
# --------------------------------------

import traceback, wrapt, time

from Log import log

'''
装饰器模块，目前提供打印完整错误日志，自动生成测试用例功能（未完善）
'''


# 单个动作方法错误日志打印
@wrapt.decorator
def error_log(wrapped, instance, args, kwargs):
	try:
		return wrapped(*args, **kwargs)
	except Exception:
		msg = traceback.format_exc()
		log.error(f'[{wrapped.__name__}]出现错误！{msg}')


# 用于函数执行错误时的重试
def retry(max_retries: int = 3, delay: (int, float) = 1):
	'''
	函数执行出现异常时的自动重试机制
	:param max_retries: 最多重试次数
	:param delay: 每次重试的延迟，单位秒
	# :param callback: 回调函数，函数签名应接收一个参数，每次出现异常时，会将异常对象传入，用于记录异常日志，中断重试等
	:return: 被装饰函数的执行结果
	'''

	@wrapt.decorator
	def wrapper(wrapped, instance, args, kwargs):
		nonlocal delay, max_retries
		times = 1
		while max_retries > 0:
			try:
				result = wrapped(*args, **kwargs)
				return result
			except Exception as msg:
				# msg = traceback.format_exc()
				log.error(f'[{wrapped.__name__}] 执行失败，原因： {msg}, 正在进行第{times}次重试……')
				max_retries -= 1
				times += 1
				if delay > 0:
					time.sleep(delay)
		else:
			log.info(f'[{wrapped.__name__}] 方法重试次数用尽，当前用例执行失败！')
	return wrapper
