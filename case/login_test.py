import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
#from ..db_fixture import test_data


class eims_login(unittest.TestCase):
    ''' 后台登录接口 '''

    def setUp(self):
        self.base_url = "http://eims.sit.datoubao.com/eims/login/loginService"


    def test_add_event_all_null(self):
        ''' 所有参数为空 '''
        payload = {'userName':'','password':'','authCode':''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['message'], '用户名或密码为空')
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        self.assertEqual(self.result['success'], False)


    def test_login_usrname_exist(self):
        ''' 错误的用户名 '''
        payload = {'userName':'errloginname','password':'admin','authCode':'0000'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['message'], '用户名或密码不正确')
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        self.assertEqual(self.result['success'], False)

    def test_login_pwd_exist(self):
        ''' 错误的密码 '''
        payload = {'userName':'admin','password':'errpwd','authCode':'0000'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['message'], '用户名或密码不正确')
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        self.assertEqual(self.result['success'], False)

    def test_authcode_error(self):
        ''' 错误的验证码 '''
        payload = {'userName': 'admin', 'password': 'admin', 'authCode': 'abcd1234'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['message'], '验证码错误')
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        self.assertEqual(self.result['success'], False)

    def test_login_success(self):
        ''' 正确登录 '''
        payload = {'userName': 'admin', 'password': 'admin', 'authCode': '0000'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'], 'admin')
        self.assertEqual(self.result['success'], True)

    def tearDown(self):
        print(str(self.result))


if __name__ == '__main__':
##    test_data.init_data()  # 初始化接口测试数据
    unittest.main()
