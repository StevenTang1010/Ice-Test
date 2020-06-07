# --------------------------------------
# Name:        expression.py
# Date:        2020-03-26
# Author:
# Description: 表达式接口操作
# --------------------------------------

from Common.Utils import error_log
from Common.Utils import es
from Log import log
from TestCase.basepage import Base


# 表达式类，继承测试基类
class Expression(Base):

	def __init__(self, ice, serverProxydict=None):
		super().__init__(ice, serverProxydict)
		self._index_dict = self.get_snapid()

	@log.logger.catch
	# 请求表达式接口
	def request_expression(self, shapid: int, key: str) -> dict:
		'''
		提供接口10481的请求
		:param snapshotid: 快照id
		:param expression: 表达式
		'''
		# 获取接口flag
		flag = self._flag_num.QUERY
		param = {
			"snapshotId": shapid,
			"key": key,
		}
		response = self.ice.request_by_user(flag=flag, params=param, token=self._token)
		if response is None:
			log.error(f'请求[{flag}]接口失败')
			raise
		else:
			return response

	@log.logger.catch
	# 解析用例结果
	def expression(self, case) -> dict:
		result_dict = {}
		case_param = case.get('expression')
		result_dict['case_param'] = case_param
		es_param = case.get('elastic')
		result_dict['es_param'] = es_param
		index_name = self._index_dict.get('index_name')
		snapshot_id = self._index_dict.get('snap_id')
		# 执行请求接口，返回表达式结果
		response = self.request_expression(snapshot_id, case_param)
		result_dict['response'] = response
		es_response = es.get_data(index_name=index_name, query=es_param)
		result_dict['es_response'] = es_response
		# cases.append(result_dict)
		# yield result_dict
		return result_dict


if __name__ == '__main__':
	pass
# test_expression('qxs-ip-167-3147-*', "'sip':'1.1.1.1'")
# ex = expressions()
# ex.expression()
