import unittest
import requests
import os, sys,time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

from db_fixture.mysql_db import DB

class Create_SecondCategory(unittest.TestCase):
    """创建二级类目"""


    def setUp(self):
        self.base_url = "http://eims.sit.datoubao.com/eims/category/createSecondCategory"
        self.table_name = "yb_category_secondary"
        self.data = {'category_name': '测试二级1'}
        db=DB()
        db.insert(table_name=self.table_name,table_data=self.data)
        db.close()


    def test_add_Category_null(self):
        ''' 全部为空 '''
        payload = {'categoryName':'','parentId':''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()

        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        self.assertEqual(self.result['success'], False)
        time.sleep(3)



    def test_add_Category_repeat(self):
        ''' 重复的二级类目 '''
        payload = {'categoryName':'测试二级1','parentId':'233'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 10001)
        self.assertEqual(self.result['message'], '该类目已存在!')
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        self.assertEqual(self.result['success'], False)
        time.sleep(3)


    def test_add_Category_success(self):
        ''' 正确的类目 '''
        payload = {'categoryName':'接口测试二级','parentId':'233'}
        r = requests.post(self.base_url, data=payload)
        self.result= r.json()
        self.assertEqual(self.result['errorCode'],0)
        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'], None)
        self.assertEqual(self.result['success'], True)

    def tearDown(self):
            self.table_name = "yb_category_secondary"
            self.data = {'category_name': '接口测试二级'}
            self.data2 = {'category_name': ''}
            db = DB()
            db.clear(table_name=self.table_name,table_data=self.data)
            db.clear(table_name=self.table_name, table_data=self.data2)
            db.close()
            print(str(self.result))

if __name__=='__main__':

    unittest.main()