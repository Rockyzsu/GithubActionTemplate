# 安装依赖 pip3 install requests html5lib bs4 schedule
import os
import requests
import json
import datetime

# 从测试号信息获取
userid = os.environ.get("USERID")
agentid = os.environ.get("AGENTID")
corpid = os.environ.get("CORPID")
corpsecret = os.environ.get("CORPSECRET")




class WeChatNotify:

    def __init__(self):
        pass

    def send_message_via_wechat(self, _message):  # 默认发送给自己

        response = requests.get(
            f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
        data = json.loads(response.text)
        access_token = data['access_token']

        json_dict = {
            "touser": userid,
            "msgtype": "text",
            "agentid": agentid,
            "text": {
                "content": _message
            },
            "safe": 0,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }
        json_str = json.dumps(json_dict)
        response_send = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}",
                                      data=json_str)
        return json.loads(response_send.text)['errmsg'] == 'ok'



def main():
    wechat = WeChatNotify()
    wechat.send_message_via_wechat("Hello, World! From github actions.{}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

if __name__ == '__main__':
    main()