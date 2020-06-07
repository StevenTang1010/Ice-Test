# --------------------------------------
# Name:        readconf.py
# Date:        2020-03-25
# Author:
# Description: 读取配置文件
# --------------------------------------

import os, configparser


# 读取配置文件
class ReadConf:
	'''
	读取配置文件：
	get_prefix：获取服务前缀
	get_db：获取数据库信息
	get_es：获取ES信息
	get_users：需要创建的用户信息
	get_center：获取中心服务器
	get_ice：获取ice服务信息
	get_cases：若存在用例参数文件，则获取内容
	:return
	'''

	def __init__(self):
		__path = os.path.join(
			os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Config'), 'config.ini')
		self.cf = configparser.ConfigParser()
		self.cf.read(__path, encoding='utf-8')

	# 获取前缀信息
	def get_prefix(self):
		prefix = self.cf.get('PREFIX_INFO', 'prefix_name')
		return prefix

	# 获取数据库配置信息
	def get_db(self):
		db_info = {}
		db_info['ip'] = self.cf.get('DB_INFO', 'db_ip')
		db_info['port'] = self.cf.getint('DB_INFO', 'db_port')
		db_info['dbname'] = self.cf.get('DB_INFO', 'db_name')
		db_info['user'] = self.cf.get('DB_INFO', 'db_user')
		db_info['pwd'] = self.cf.get('DB_INFO', 'db_pwd')
		return db_info

	# 获取es配置信息
	def get_es(self):
		es_info = {}
		es_info['ip'] = self.cf.get('ES_INFO', 'ip')
		es_info['port'] = self.cf.get('ES_INFO', 'port')
		es_info['user'] = self.cf.get('ES_INFO', 'user')
		es_info['pwd'] = self.cf.get('ES_INFO', 'pwd')
		es_info['timeout'] = self.cf.getint('ES_INFO', 'timeout')
		return es_info

	# 获取登陆用户名密码信息
	def get_users(self):
		user_info = {}
		user_info['username'] = self.cf.get('USER_INFO', 'username')
		user_info['pwd'] = self.cf.get('USER_INFO', 'pwd')
		return user_info

	# 获取中心服务器信息
	def get_center(self):
		center_info = {}
		center_info['ip'] = self.cf.get('CENTER_INFO', 'center_ip')
		center_info['user'] = self.cf.get('CENTER_INFO', 'center_user')
		center_info['pwd'] = self.cf.get('CENTER_INFO', 'center_pwd')
		return center_info

	# 获取ice配置信息
	def get_ice(self):
		ice_info = {}
		ice_info['object'] = self.cf.get('ICE_INFO', 'ice_object')
		ice_info['ip'] = self.cf.get('ICE_INFO', 'ice_ip')
		ice_info['port'] = self.cf.get('ICE_INFO', 'ice_port')
		return ice_info

	# 获取工程配置信息
	def get_prj(self):
		prj_info = {}
		prj_info['prjname'] = self.cf.get('PRJ_INFO', 'prjname')
		prj_info['snapname'] = self.cf.get('PRJ_INFO', 'snapname')
		return prj_info

conf_info = ReadConf()
