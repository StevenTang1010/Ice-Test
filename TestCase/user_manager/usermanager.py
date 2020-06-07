# -*- coding: utf-8 -*-

# --------------------------------------
# Name:        usermanager.py
# Date:        2020-04-26
# Author:      
# Description: 用户管理模块
# --------------------------------------

# 表达式类，继承测试基类
import hashlib

from Common.Utils import error_log
from Log import log
from TestCase.basepage import Base


# 用户管理，继承基类
class UserManager(Base):
	@log.logger.catch
	# 请求添加用户接口
	def add_user(self, userdict):
		'''
		提供接口10001的请求
		:param userdict: 用户信息
		'''

		flag = self._flag_num.ADD_USER
		_login_name = userdict.get('username')
		param = {
			"loginName": _login_name,
			"loginPwd": hashlib.md5(str(userdict.get('pwd')).encode(encoding='utf8')).hexdigest(),
			"userName": _login_name,
			"roleId": userdict.get('roleid'),
			"userState": 1,
			"isRoot": 1
		}
		# response = self.ice.request(flag=flag, params=param)
		response = self.ice.request_by_user(flag=flag, params=param, token=self._token)
		if response is None:
			log.error(f'请求[{flag}]接口失败')
		else:
			db_len = len(self.do_select(f'select user_id from sys_user where login_name="{_login_name}";'))
			return response, db_len

	# 请求删除用户接口
	@log.logger.catch
	def del_user(self, userdict):
		'''
		提供接口10002的请求
		:param userdict: 用户信息
		'''
		_login_name = userdict.get('username')
		result = self.do_select(f'select user_id from sys_user where login_name="{_login_name}";')
		user_id = result[0][0]
		flag = self._flag_num.DEL_USER
		param = {
			'userId': [user_id, ]
		}
		response = self.ice.request_by_user(flag=flag, params=param, token=self._token)
		if response is None:
			log.error(f'请求[{flag}]接口失败')
			raise
		else:
			db_len = len(self.do_select(f'select user_id from sys_user where login_name="{_login_name}";'))
			self.do_delete(f'delete from sys_user where user_name="{_login_name}"')
			return response, db_len
