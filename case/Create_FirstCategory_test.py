import unittest
import requests
import os, sys,time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, parentdir)
sys.path.append("..")

from db_fixture.mysql_db import DB


class eims_login(unittest.TestCase):
    ''' 后台创建一级类目  接口 '''

    def setUp(self):
        self.base_url = "http://eims.sit.datoubao.com/eims/category/createFirstCategory"
        self.table_name = "yb_category_primary"
        self.data = {'category_name': '一级类目'}
        db=DB()
        db.insert(table_name=self.table_name,table_data=self.data)
        db.close()

    def test_add_Category_repeat(self):
        ''' 重复的类目 '''
        payload = {'categoryName':'一级类目'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 10001)
        self.assertEqual(self.result['message'], '该类目已存在!')
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        self.assertEqual(self.result['success'], False)
        time.sleep(3)
        print(r.json())

    def test_add_Category_success(self):
            ''' 正确的类目 '''
            payload = {'categoryName': '接口测试2'}
            r = requests.post(self.base_url, data=payload)
            self.result = r.json()
            self.assertEqual(self.result['errorCode'], 0)
            self.assertEqual(self.result['message'], None)
            self.assertEqual(self.result['result'], True)
            self.assertEqual(self.result['resultObject'], None)
            self.assertEqual(self.result['success'], True)

    def test_add_Category_False(self):
            ''' 错误的参数 '''
            payload = {'username': 'xxxx'}
            r = requests.post(self.base_url, data=payload)
            self.result = r.json()
            self.assertEqual(self.result['error'], 'Bad Request')
            self.assertEqual(self.result['message'], "Required String parameter 'categoryName' is not present")
            self.assertEqual(self.result['status'], 400)

    # self.assertEqual(self.result['resultObject'], None)
    #        self.assertEqual(self.result['success'], False)

    def tearDown(self):

        self.table_name = "yb_category_primary"
        self.data = {'category_name': '接口测试2'}
        self.data2 = {'category_name': '一级类目'}
        db = DB()
        db.clear(table_name=self.table_name,table_data=self.data)
        db.clear(table_name=self.table_name, table_data=self.data2)
        db.close()

        print(str(self.result))



if __name__=='__main__':

    unittest.main()