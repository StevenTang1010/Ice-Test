# -*- coding: utf-8 -*-

# --------------------------------------
# Name:        blackinfo.py
# Date:        2020-04-29
# Author:
# Description: 特征管理
# --------------------------------------

# 表达式类，继承测试基类
import hashlib

from Common.Utils import error_log
from Log import log
from TestCase.basepage import Base


# 黑IP/DNS，继承基类
class BlackData(Base):
	@log.logger.catch
	# 请求添加黑IP接口
	def add_blackip(self, blackipdict):
		flag = self._flag_num.ADD_BLACK
		_black_ip = blackipdict.get('ip')
		param = {"type": 1, "value": [
			{
				"id": None,
				"blackDomain": None,
				"blackIp": _black_ip,
				"description": blackipdict.get('remark'),
				"createTime": None,
				"userId": self._userId,
				"buildType": None
			}
		]}
		response = self.ice.request_by_user(flag=flag, params=param, token=self._token)
		if response is None:
			log.error(f'请求[{flag}]接口失败')
		else:
			db_len = len(self.do_select(f'select id from pro_black_ip where black_ip="{_black_ip}";'))
			return response, db_len

	@log.logger.catch
	# 请求删除黑IP接口
	def del_blackip(self, blackipdict):
		flag = self._flag_num.DEL_BLACK
		_black_ip = blackipdict.get('ip')
		black_id = self.do_select(f'select id from pro_black_ip where black_ip="{_black_ip}";')[0][0]
		param = {"userId": 104, "type": 1, "id": [black_id]}
		response = self.ice.request_by_user(flag=flag, params=param, token=self._token)
		if response is None:
			log.error(f'请求[{flag}]接口失败')
		else:
			db_len = len(self.do_select(f'select id from pro_black_ip where black_ip="{_black_ip}";'))
			return response, db_len

	@log.logger.catch
	# 请求添加黑域名接口
	def add_blackdns(self, blackdnsdict):
		flag = self._flag_num.ADD_BLACK
		_black_domain = blackdnsdict.get('dns')
		param = {"type": 1, "value": [
			{
				"id": None,
				"blackDomain": _black_domain,
				"blackIp": None,
				"description": blackdnsdict.get('remark'),
				"createTime": None,
				"userId": self._userId,
				"buildType": None
			}
		]}
		response = self.ice.request_by_user(flag=flag, params=param, token=self._token)
		if response is None:
			log.error(f'请求[{flag}]接口失败')
		else:
			db_len = len(self.do_select(f'select id from pro_black_domain where black_domain="{_black_domain}";'))
			return response, db_len

	@log.logger.catch
	# 请求删除黑域名接口
	def del_blackdns(self, blackdnsdict):
		flag = self._flag_num.DEL_BLACK
		_black_domain = blackdnsdict.get('dns')
		black_id = self.do_select(f'select id from pro_black_domain where black_domain="{_black_domain}";')[0][0]
		param = {"userId": 104, "type": 1, "id": [black_id]}
		response = self.ice.request_by_user(flag=flag, params=param, token=self._token)
		if response is None:
			log.error(f'请求[{flag}]接口失败')
		else:
			db_len = len(self.do_select(f'select id from pro_black_domain where black_domain="{_black_domain}";'))
			return response, db_len
