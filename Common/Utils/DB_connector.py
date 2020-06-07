# --------------------------------------
# Name:        DB_connector.py
# Date:        2020-03-25
# Author:      Steven_Tang
# Description: MySql操作封装
# --------------------------------------

from Common.Config.readconf import conf_info
from Log import log
import pymysql
from Common.Utils.Decorator import *


class MysqlDB:
	'''
	数据库操作库，封装了一系列数据库操作方法
	'''

	def __init__(self):
		__database = conf_info.get_db()
		config = {
			'host': __database['ip'],
			'user': __database['user'],
			'password': __database['pwd'],
			'port': __database['port'],
			'database': __database['dbname'],
			'charset': 'utf8',
			'autocommit': True
		}
		try:
			log.info(f"正在连接数据库>>>>>>>>>>>")
			self.db = pymysql.connect(**config)
		except Exception as e:
			log.error(e)
		else:
			self.cursor = self.db.cursor()
			log.info(f"连接 [{__database['dbname']}] 数据库成功!")

	def __getattribute__(self, item):
		if item in ('select', 'delete', 'update', 'insert'):
			log.debug(f'>>>[{self}.{item}]')
		return object.__getattribute__(self, item)

	# 查询
	@log.logger.catch
	def select(self, sql):
		try:
			log.info(f'正在执行sql: {sql}')
			self.cursor.execute(sql)
			# self.db.commit()
		except Exception as e:
			log.error(f'操作失败！ {str(e)}')
		else:
			result = self.cursor.fetchall()
			if result is not None:
				log.info(f'查询成功！ 查询到 {len(result)} 条结果！')
				return list(result)
			else:
				return []

	# 删除
	@log.logger.catch
	def delete(self, sql):
		try:
			log.info(f'正在执行sql: {sql}')
			self.cursor.execute(sql)
		except Exception as e:
			log.error(f"发生错误 {str(e)} ，将进行回滚！")
			self.db.rollback()  # 发生错误回滚
		else:
			self.db.commit()
			log.info('操作成功！')

	# 新增和更新
	@log.logger.catch
	def update(self, sql):
		try:
			log.info(f'正在执行sql: {sql}')
			self.cursor.execute(sql)
		except Exception as e:
			log.error(f'操作失败！ {str(e)}')
		else:
			log.info('更新表成功！')

	# 插入
	@log.logger.catch
	def insert(self, sql):
		try:
			log.info(f'正在执行sql: {sql}')
			self.cursor.execute(sql)
		except Exception as e:
			log.error(f"发生错误 {str(e)} ，将进行回滚！")
			self.db.rollback()
		else:
			self.db.commit()
			log.info('操作成功！')

	# 析构函数
	def __del__(self):
		self.db.close()


db = MysqlDB()
#
if __name__ == '__main__':
	cases = db.select(
		'select user_id from sys_user where login_name="root";')
	# print(cases[0][0])
	print(cases)
