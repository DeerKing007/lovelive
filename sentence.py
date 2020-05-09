import requests


class Daily_Sentence:
    def __init__(self):
        self.dictum_channel_name = {1: '词霸(每日英语)', 2: '土味情话'}

    def isJson(self, resp):
        '''
        判断数据是否能被 Json 化。 True 能，False 否。
        :param resp: request
        :return: bool, True 数据可 Json 化；False 不能 JOSN 化。
        '''
        try:
            resp.json()
            return True
        except:
            return False

    def get_ciba_info(self):
        '''
        从词霸中获取每日一句，带英文。
        :return:str ,返回每日一句（双语）
        '''
        print('获取格言信息（双语）...')
        resp = requests.get('http://open.iciba.com/dsapi')
        if resp.status_code == 200 and self.isJson(resp):
            conentJson = resp.json()
            content = conentJson.get('content')
            note = conentJson.get('note')
            return f"{content}\n{note}\n"
        else:
            print("没有获取到数据")
            return None

    def get_lovelive_info(self):
        '''
        从土味情话中获取每日一句。
        :return: str,土味情话
        '''
        print('获取土味情话...')
        resp = requests.get("https://api.lovelive.tools/api/SweetNothings")
        if resp.status_code == 200:
            return resp.text + "\n"
        else:
            print('每日一句获取失败')
        return None


if __name__ == '__main__':
    ds = Daily_Sentence()
    print(ds.get_ciba_info())
    print(ds.get_lovelive_info())