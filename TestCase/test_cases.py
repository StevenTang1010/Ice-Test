# -*- coding:utf-8 -*-
from os import path

import pytest
from yaml import safe_load

from Log import log


class TestSuit:
	# 测试表达式接口
	@pytest.mark.skip
	@pytest.mark.parametrize('case', safe_load(open(
		path.join(path.join(path.dirname(path.abspath(__file__)), 'case_yaml'), 'expression.yaml'))))
	def test_expression(self, expression_setup, case: dict):
		result = expression_setup.expression(case)
		# 遍历从生成器返回的所有用例结果
		response = result.get('response')
		es_response = result.get('es_response')
		case_param = result.get('case_param')
		try:
			# 第一次断言状态
			assert response.get('status')
			status_code = response.get('status')
			if status_code != 200:
				log.error(f'{case_param} 参数请求失败！ 原因：服务器响应不正确，status_code={status_code}')
			else:
				# 提取返回数量第二次断言
				api_total = response.get('value').get('total')
				es_total = es_response.get('hits').get('total')
				try:
					assert api_total == es_total
				except:
					log.error(f'{case_param} 用例验证失败！ 原因：数据返回与ES不匹配，接口返回：({api_total})，ES返回：({es_total})')
		except Exception as e:
			log.info(f'{case_param} 请求失败，结果为空！{e}')

	# 测试添加用户接口
	# @pytest.mark.skip
	@pytest.mark.parametrize('userdict', safe_load(open(
		path.join(path.join(path.dirname(path.abspath(__file__)), 'case_yaml'), 'adduser.yaml'))))
	def test_add_user(self, user_manager_setup, userdict: dict):
		response, db_len = user_manager_setup.add_user(userdict)
		assert response.get('status') == 200
		assert db_len > 0

	# 测试删除用户接口
	# @pytest.mark.skip
	@pytest.mark.parametrize('userdict', safe_load(open(
		path.join(path.join(path.dirname(path.abspath(__file__)), 'case_yaml'), 'adduser.yaml'))))
	def test_del_user(self, user_manager_setup, userdict: dict):
		response, db_len = user_manager_setup.del_user(userdict)
		assert response.get('status') == 200
		assert db_len == 0

	# 测试添加黑IP接口
	# @pytest.mark.skip
	@pytest.mark.parametrize('blackipdict', safe_load(open(
		path.join(path.join(path.dirname(path.abspath(__file__)), 'case_yaml'), 'blackdata.yaml'))))
	def test_add_black_ip(self, rule_manager_setup, blackipdict: dict):
		response, db_len = rule_manager_setup.add_blackip(blackipdict)
		assert response.get('status') == 200
		assert db_len == 0

	# 测试删除黑IP接口
	# @pytest.mark.skip
	@pytest.mark.parametrize('blackipdict', safe_load(open(
		path.join(path.join(path.dirname(path.abspath(__file__)), 'case_yaml'), 'blackdata.yaml'))))
	def test_del_black_ip(self, rule_manager_setup, blackipdict: dict):
		response, db_len = rule_manager_setup.del_blackip(blackipdict)
		assert response.get('status') == 200
		assert db_len == 0

	# 测试添加黑域名接口
	# @pytest.mark.skip
	@pytest.mark.parametrize('blackipdict', safe_load(open(
		path.join(path.join(path.dirname(path.abspath(__file__)), 'case_yaml'), 'blackdata.yaml'))))
	def test_add_black_dns(self, rule_manager_setup, blackipdict: dict):
		response, db_len = rule_manager_setup.add_blackdns(blackipdict)
		assert response.get('status') == 200
		assert db_len == 0

	# 测试删除黑域名接口
	# @pytest.mark.skip
	@pytest.mark.parametrize('blackipdict', safe_load(open(
		path.join(path.join(path.dirname(path.abspath(__file__)), 'case_yaml'), 'blackdata.yaml'))))
	def test_del_black_dns(self, rule_manager_setup, blackipdict: dict):
		response, db_len = rule_manager_setup.del_blackdns(blackipdict)
		assert response.get('status') == 200
		assert db_len == 0


if __name__ == '__main__':
	case_path = path.join(path.join(path.dirname(path.abspath(__file__)), 'case_yaml'), 'expression.yaml')
	print(case_path)
