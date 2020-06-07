# --------------------------------------
# Name:        Ice_connector.py
# Date:        2020-03-25
# Author:
# Description: 封装用例公共方法
# --------------------------------------
from Log import log
from Common.Utils import db


# 作为所有模块的基类,封装公共方法
class Base:

	def __init__(self, ice, serverProxydict=None):
		# ice连接对象
		self.ice = ice
		# 接口flag
		self._flag_num = self.ice.flag_num
		# 工程信息
		self._prj_info = self.ice.prj_info
		# 登陆信息
		self._serverProxydict = serverProxydict
		_username = list(self._serverProxydict.keys())[0]
		self._token = self._serverProxydict.get(_username).get('token')
		self._userId = self._serverProxydict.get(_username).get('userid')

	def __getattribute__(self, item):
		if item in ('get_snapid',):
			log.debug(f'>>>[{self}.{item}]')
		return object.__getattribute__(self, item)

	# 数据库查询封装
	def do_select(self, sql):
		return db.select(sql)

	# 数据库删除封装
	def do_delete(self, sql):
		db.delete(sql)

	# 获取工程、快照id和es索引名
	def get_snapid(self) -> dict:
		prjname = self._prj_info.get('prjname')
		snapname = self._prj_info.get('snapname')
		index_dict = {}
		sql = f'select project_id from prj where prjnm="{prjname}";'
		prjid = self.do_select(sql)[0][0]
		# index_dict['prj_id'] = prjid
		sql = f'select snapshot_id from sht where project_id={prjid} and shtnm="{snapname}";'
		snapid = self.do_select(sql)[0][0]
		index_dict['snap_id'] = snapid
		sql = f'select snapshot_index from sht where project_id={prjid} and shtnm="{snapname}";'
		esindex = self.do_select(sql)[0][0].replace('"', '').replace('[', '').replace(']', '')
		index_dict['index_name'] = esindex
		return index_dict
