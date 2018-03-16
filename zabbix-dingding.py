#!/usr/bin/env python
#coding=utf8
# Author:   jikun.zhang@edaibu.net
# buid by :zjk
import requests
import json
import sys
import os
import time
import configparser
'''zabbix告警脚本参数：1.{ALERT.SENDTO} 2.{ALERT.MESSAGE}
权限及日志配置
touch /var/log/zabbix/zabbix_dingding.log
chmod 770 /var/log/zabbix/zabbix_dingding.log
chown zabbix:zabbix /var/log/zabbix/zabbix_dingding.log
chmod 770 /etc/zabbix/dingding.conf
chown zabbix:zabbix /etc/zabbix/dingding.conf
chmod 770 /usr/lib/zabbix/alertscripts/zabbix-dingding.py
chown zabbix:zabbix /usr/lib/zabbix/alertscripts/zabbix-dingding.py

'''
headers = {'Content-Type': 'application/json'}
time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
config=configparser.ConfigParser()
config.read('/etc/zabbix/dingding.conf')
log_file = config.get('config','log')
api_url = config.get('config','webhook')

def log(info):
    if os.path.isfile(log_file) == False:
               f = open(log_file, 'a+')
    f = open(log_file,'a+')
    f.write(info)
    f.close()
    
def msg(text,user):
    json_text= {
     "msgtype": "markdown",
     "markdown": {
         "title": "智享云告警信息",
         "text": text
         },
     "at": {
         "atMobiles": [
             user
             ],
         "isAtAll": True
         }
     }
    print json_text
    r=requests.post(api_url,data=json.dumps(json_text),headers=headers).json()
    code = r["errcode"]
    if code == 0:
        log(time + ":消息发送成功 返回码:" + str(code) + "\n")
    else:
        log(time + ":消息发送失败 返回码:" + str(code) + "\n")
        exit(3)

if __name__ == '__main__':
    text = sys.argv[2]
    user = sys.argv[1]
    msg(text,user)
'''
需要安装模块：requests  json configparser
告警内容参考：
操作-----------
##### [智享云告警平台信息](http://192.168.1.158:8000/zabbix)
#### {TRIGGER.NAME}
###### 故障时间：{EVENT.DATE} {EVENT.TIME}
###### 故障时长：{EVENT.AGE}
###### 告警级别：{TRIGGER.SEVERITY}
###### 故障事件ID：{EVENT.ID}
###### 故障主机IP：{HOST.IP}
###### 故障主机名：{HOST.NAME}
###### 故障是否确认：{EVENT.ACK.STATUS}
#### {ITEM.LASTVALUE}
##### ![screenshot](http://www.zxbike.cn/template/zxbike/images/logo.png)

恢复操作
##### [智享云告警平台信息](http://192.168.1.158:8000/zabbix)
#### {TRIGGER.NAME} 已经恢复
###### 恢复时间：{EVENT.RECOVERY.DATE} {EVENT.RECOVERY.TIME} 
###### 故障时长：{EVENT.AGE}
###### 当前状态：{EVENT.STATUS}
###### 故障事件ID：{EVENT.ID}
###### 故障主机IP：{HOST.IP}
###### 故障主机名：{HOST.NAME}
###### 故障是否确认：{EVENT.ACK.STATUS}
#### {ITEM.LASTVALUE}
##### ![screenshot](http://www.zxbike.cn/template/zxbike/images/logo.png)

确认操作
##### [智享云告警平台信息](http://192.168.1.158:8000/zabbix)
#### 管理员{USER.FULLNAME} 已经发布故障原因
###### 确认时间：{ACK.DATE} {ACK.TIME} 
###### 故障时长：{EVENT.AGE}
###### 当前状态：{EVENT.STATUS}
###### 故障事件ID：{EVENT.ID}
###### 故障主机IP：{HOST.IP}
###### 故障主机名：{HOST.NAME}
###### 故障是否确认：{EVENT.ACK.STATUS}
###### 故障前状态：{ITEM.LASTVALUE}
{ACK.MESSAGE}
##### ![screenshot](http://www.zxbike.cn/template/zxbike/images/logo.png)
'''