import requests


class test():

    def __init__(self):
        self.base_url = "http://yanbao.admin.datoubao.com/eims/login/loginService"

    def test_add_event_all_null(self):
            ''' 所有参数为空 '''
            payload = {'userName': '', 'password': '', 'authCode': ''}
            r = requests.post(self.base_url, payload)


            print(r.json())



if __name__=='__main__':
    test().test_add_event_all_null()