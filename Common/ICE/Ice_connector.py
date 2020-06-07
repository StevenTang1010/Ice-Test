# --------------------------------------
# Name:        Ice_connector.py
# Date:        2020-03-25
# Author:
# Description: ICE接口连接登陆
# --------------------------------------

import json, hashlib
import sys, traceback, Ice

from Common.Config import flag_num
from Common.Config.readconf import conf_info
from Log import log
from Common.ICE import common_ice
from Common.Utils import Decorator
import time


# ICE控制登陆类
class Icecheck:

	def __init__(self):
		log.info('初始化ICE连接'.center(70, '='))
		self.user_info = conf_info.get_users()
		self.flag_num = flag_num
		self.prj_info = conf_info.get_prj()
		self.ice_info = conf_info.get_ice()
		self._serverProxy = self._connet_ice_server()
		if self._serverProxy is None:
			log.error('ICE连接失败，请重试！'.center(60, '='))
			raise

	def __getattribute__(self, item):
		if item in ('_connet_ice_server', 'login_ice', 'logout_ice', 'request', 'request_by_user'):
			log.debug(f'>>>[{self}.{item}]')
		return object.__getattribute__(self, item)

	# 连接ICE服务，生成接口对象
	@Decorator.retry()
	def _connet_ice_server(self):
		try:
			ic = Ice.initialize(sys.argv)
			proxyString = ic.stringToProxy(
				f"{self.ice_info['object']}: default -h {self.ice_info['ip']} -p {self.ice_info['port']}")
			proxy = ic.stringToProxy(str(proxyString))
			log.info(f"正在连接ICE服务： {proxyString}")
			serverProxy = common_ice._M_common.CommonServicePrx.checkedCast(proxy)
			serverProxy.ice_ping()
			if not serverProxy:
				log.error("ICE服务连接失败！")
				log.info("".center(80, '='))
				raise RuntimeError
			else:
				log.info(f"ICE服务连接成功，地址：{self.ice_info['ip']}, 端口：{self.ice_info['port']}")
				log.info("".center(80, '='))
				return serverProxy
		except:
			traceback.print_exc()

	# 使用给定用户调用登陆接口登陆ice服务
	@Decorator.retry()
	# 登陆指定账号服务器
	def login_ice(self, identity=None) -> dict:
		'''
		:return 返回接口请求结果，包含userid和token
		'''
		loginname = self.user_info.get('username')
		loginpwd = self.user_info.get('passwd')
		if not identity:
			identity = {"name": "auto_test", "category": ""}
		# 定义参数内容
		dictParams = {
			"loginName": loginname,
			"loginPwd": hashlib.md5(loginpwd.encode(encoding='utf8')).hexdigest(),
			"identity": identity
		}
		# json格式化
		paramsStr = json.dumps(dictParams)
		log.info(f"[{loginname}]>>>>>>>>>>>正在登陆<<<<<<<<<<<< ")
		ret = self._serverProxy.request(self.flag_num.LOGIN, paramsStr)
		retDict = json.loads(ret)
		if retDict.get('status') == 500:
			log.error(f'登陆失败！ 原因：{retDict.get("msg")}，停止测试')
			raise
		elif retDict.get('status') != 200:
			log.error(f'登陆失败！ 原因：{retDict.get("msg")}')
			log.info("".center(80, '=') + '\n')
			return retDict
		else:
			dictvalue = retDict.get('value')
			token = dictvalue.get('token')
			userid = dictvalue.get('userId')
			# 返回用户登陆信息
			serverProxydict = {}
			serverProxydict[self.user_info['username']] = {
				'userid': userid,
				'token': str(token)
			}
			log.info(f"[{loginname}] 登陆成功！{retDict}")
			log.info("".center(80, '=') + '\n')
			return serverProxydict

	# 用户登出
	def logout_ice(self, serverProxydict):
		# 如果用户已经登出，则不再登出
		if serverProxydict is None:
			log.info('用户已经登出')
			return
		else:
			userinfo = list(serverProxydict.values())[0]
			username = userinfo.get('username')
			log.info(f'用户 {username} 正在登出！')
			paramDict = {'userId': userinfo.get('userid')}
			self.request_by_user(self.flag_num.LOGOUT, paramDict, token=userinfo.get('token'))
			serverProxydict.clear()

	# 不包含用户信息的请求方法
	@Decorator.retry()
	def request(self, flag: int, params: dict) -> dict:
		self._serverProxy.ice_ping()
		# 字典转化为json字符串
		paramsStr = json.dumps(params)
		log.info(f'开始请求接口： {flag}， 参数: {paramsStr}')
		s_time = time.time()
		ret = self._serverProxy.request(flag, paramsStr)
		e_time = time.time()
		log.info(f'本次请求耗时： {e_time - s_time}')
		# 字符串转化为字典返回
		retDict = json.loads(ret)
		log.info(f"请求成功！status: {retDict.get('status')}, msg:{retDict.get('msg')}")
		return retDict

	# 包含用户登录信息的接口请求方法
	@Decorator.retry()
	def request_by_user(self, flag: int, params: dict, token) -> dict:
		self._serverProxy.ice_ping()
		# 字典转化为json字符串
		paramsStr = json.dumps(params)
		_ctx = {'token': token}
		log.info(f'开始请求接口： {flag}， 参数: {paramsStr}')
		s_time = time.time()
		ret = self._serverProxy.request(flag, paramsStr, _ctx)
		e_time = time.time()
		log.info(f'本次请求耗时： {e_time - s_time}')
		# 字符串转化为字典返回
		retDict = json.loads(ret)
		msg = retDict.get('msg')
		if msg and 'token无效' in msg:
			log.error(f'请求错误,原因： {msg}')
			response = self.login_ice()
			token = response.get(self.user_info['username']).get('token')
			ret = self.request_by_user(flag, params, token)
			return ret
		else:
			log.info(f"请求成功！status: {retDict.get('status')}, msg:{retDict.get('msg')}")
			return retDict


ice = Icecheck()

if __name__ == '__main__':
	pass
	# ic = Icecheck()
	# ic.logout_ice()
