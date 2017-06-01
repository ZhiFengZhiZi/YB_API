import unittest
import requests
import os, sys,time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class CreateProduct(unittest.TestCase):
    ''' 保存产品基本信息'''

    def SetUp(self):
        url ="http://eims.sit.datoubao.com/eims/product/saveProductInfo"
        res = requests.request("POST", url, )
        print(res.text)
        self.assertEqual(res['result'],'true')
        self.assertEqual(res['message'],'null')
        self.assertEqual(res['errorCode'], 0)
        self.assertEqual(res['success'],'true')



if __name__=='__main__':

    unittest.main()