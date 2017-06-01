import unittest
import requests
import os, sys,time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class CreateProduct(unittest.TestCase):
     def SetUp(self):
        url ="http://eims.sit.datoubao.com/eims/channel/queryChannelTree"
        res = requests.request("POST", url, )
        print(res.text)
        self.assertEqual(res['result'],'true')
        self.assertEqual(res['message'],'null')
        self.assertEqual(res['errorCode'], 0)
        self.assertEqual(res['success'],'true')






if __name__=='__main__':
    unittest.main()
