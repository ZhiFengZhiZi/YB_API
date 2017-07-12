import unittest
import requests
import os, sys,time
from db_fixture.mysql_db import DB
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)



class Create_ThirdCategory(unittest.TestCase):
    ''' 后台创建三级类目    接口 '''

    def setUp(self):
        self.base_url = "http://eims.sit.datoubao.com/eims/category/createThirdCategory"


    def test_add_Category_null(self):
        ''' 全部为空 '''
        payload = {'categoryName':'','parentId':''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        self.assertEqual(self.result['success'], False)
        time.sleep(3)

    def test_add_Category_parentIDnull(self):
        ''' 二级类目id为空 '''
        payload = {'categoryName':'三级类目xx','parentId':''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        self.assertEqual(self.result['success'], False)
        time.sleep(3)

    def test_add_Category_categoryNamenull(self):
        ''' 三级类目名称为空 '''
        payload = {'categoryName': '', 'parentId': '60'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        self.assertEqual(self.result['success'], False)
        time.sleep(3)

    def test_add_Category_repeat(self):
        ''' 重复的三级类目 '''
        payload = {'categoryName':'三级类目','parentId':'60'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 10001)
        self.assertEqual(self.result['message'], '该类目已存在!')
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        self.assertEqual(self.result['success'], False)
        time.sleep(3)


    def test_add_OneCategory_wrong(self):
        ''' 错误的二级类目ID'''
        payload = {'categoryName':'三级类目','parentId':'888888'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['resultObject'], None)
        self.assertEqual(self.result['success'], False)
        time.sleep(3)


    def test_add_Category_success(self):
        ''' 正确的类目 '''
        payload = {'categoryName':'三级类目no','parentId':'60'}
        r = requests.post(self.base_url, data=payload)
        self.result= r.json()
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['resultObject'], None)
        self.assertEqual(self.result['success'], True)


    def tearDown(self):
            self.table_name = "yb_category_thirdly"
            self.data = {'category_name': '三级类目'}
            self.data2 = {'category_name': '三级类目no'}
            db = DB()
            db.clear(table_name=self.table_name,table_data=self.data)
            db.clear(table_name=self.table_name, table_data=self.data2)
            db.close()
            print(str(self.result))

if __name__=='__main__':

    unittest.main()