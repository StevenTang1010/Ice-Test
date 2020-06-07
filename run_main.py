# -*- coding: utf-8 -*-

# --------------------------------------
# Name:        run_main.py
# Date:        2020-04-21
# Author:
# Description: 主函数，执行用例
# --------------------------------------
import pytest

from Log import log

if __name__ == '__main__':
	log.info('测试开始'.center(70, '>'))

	import os

	case_path = os.path.join(os.path.join(os.getcwd()), 'Report')
	# html_report_path = os.path.join(case_path, 'report.html')
	html_report_path = os.path.join(case_path, 'html')
	xml_report_path = os.path.join(case_path, 'xml')

	# pytest 运行测试
	argv = ['-v', '-s', f'--alluredir={xml_report_path}', '--clean-alluredir']
	#
	# # 失敗重试机制
	# argv.append('--reruns={}'.format(1))
	# argv.append('--reruns-delay={}'.format(3))
	#
	# # 分布执行机制
	# argv.append('-n 20')
	#
	# # 运行某一个用例或者类
	# # argv.append(
	# #     "F:\\ui_test\\testcases\\threat_awareness_center\\terminal\\Feature_system\\SignNet\\"
	# #     "test_BlackFeature_domain.py::Test_BlackManage_domain4::test_BlackManage_domain_search_node_button_unselect")
	# # argv.append(
	# #     "F:\\ui_test\\testcases\\threat_awareness_center\\network_equipment\\RouterNode_system\\RouterDataFlow")
	# # argv.append(
	# #     r"F:\ui_test\testcases\threat_awareness_center\network_equipment\RouterNode_system\RouterDataFlow")
	#
	# argv.append(
	#
	# 	r"F:\0068-NetDA\08Code\ui_test\testcases\threat_awareness_center\network_equipment\RouterNode_system\RouterDataFlow")
	#
	pytest.main(argv)

	# 生成allure报告
	cmd = f'allure generate {xml_report_path} -o {html_report_path} --clean'
	try:
		os.popen(cmd)
		log.info(f"  ******  开始生成测试报告  ******  \n {cmd}")
	except Exception as e:
		log.error(u'生成allure报告失败，请检查环境配置', e)
	log.info('测试完成,请查看报告!'.center(40, '<'))

	cmd = f'allure serve {xml_report_path}'
	os.popen(cmd)
	log.info('打开测试报告')
