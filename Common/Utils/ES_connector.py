# --------------------------------------
# Name:        ES_connector.py
# Date:        2020-03-25
# Author:
# Description: ES操作封装
# --------------------------------------

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from Common.Config.readconf import conf_info
from Log import log
import random
import string
from Common.Utils import error_log


class ElasticClient:

	def __init__(self):
		es_info = conf_info.get_es()
		es_url = f"http://{es_info.get('user')}:{es_info.get('pwd')}" \
			f"@{es_info.get('ip')}:{es_info.get('port')}"
		self.es = Elasticsearch(es_url, timeout=es_info.get('timeout'))

	def __getattribute__(self, item):
		if item in ('get_data', 'insert_data'):
			log.debug(f'>>>[{self}.{item}]')
		return object.__getattribute__(self, item)

	# 查询数据
	@log.logger.catch
	def get_data(self, index_name, query):
		'''
		根据传入的索引名及查询语句查询es数据
		:param index_name: 索引名,  query: 查询语句
		:return 返回es查询结果
		'''
		data = self.es.search(index=index_name, body={"query": {"query_string": {"query": query}}})
		log.info(f"ES请求成功！返回值{data.get('hits').get('total')}")
		return data

	# 插入数据
	@log.logger.catch
	def insert_data(self, index_name, index_type, sources):
		'''
		批量插入es数据
		:param index_name: 索引名
		:param index_type: 索引类型
		:param sources: 数据内容
		数据内容尽量不超过100条，多线程写入，ES性能有限
		'''
		actions = []
		for source in sources:
			index_id = ''.join(random.sample(string.digits + string.ascii_lowercase, 22))
			action = {
				"_index": index_name,
				"_type": index_type,
				"_id": index_id,
				"_source": source
			}
			actions.append(action)
		success, failed = bulk(self.es, actions=actions, chunk_size=len(actions), request_timeout=100,
		                       raise_on_error=True)
		log.info(f"索引:{index_name},成功插入的数据个数:{success}")
		log.error(f"索引:{index_name},插入失败的数据个数:{failed}")


es = ElasticClient()

if __name__ == "__main__":
	pass
	# print(es.get_data('qxs-ip-166-3128-*', '"outb:>10000 AND inb:>10000"'))
