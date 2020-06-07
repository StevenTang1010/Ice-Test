import pytest

from Common.ICE.Ice_connector import ice

global serverProxydict


@pytest.fixture(scope='module', autouse=True)
def login_ice():
	# µÇÂ½ÕËºÅ
	global serverProxydict
	serverProxydict = ice.login_ice()
	yield
	ice.logout_ice(serverProxydict)


@pytest.fixture(scope='class')
def expression_setup():
	global serverProxydict
	from TestCase.expressions.expression import Expression
	return Expression(ice, serverProxydict)


@pytest.fixture(scope='class')
def user_manager_setup():
	global serverProxydict
	from TestCase.user_manager.usermanager import UserManager
	return UserManager(ice, serverProxydict)


@pytest.fixture(scope='class')
def rule_manager_setup():
	global serverProxydict
	from TestCase.rule_manager.blackinfo import BlackData
	return BlackData(ice, serverProxydict)
