#!/usr/bin/env python
import paramiko
import time
import atexit
_active_threads = []
def _join_lingering_threads():
    for thr in _active_threads:
        thr.stop_thread()

username = "root"
password = "Aa123456789"
hostname = "192.168.1.35"
port = "22"
try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname, port, username, password)
    client.exec_command('cd /root')
    print("開啟網站....")
    stdin, stdout, stderr = client.exec_command('systemctl start nginx')
    result = stdout.readlines()
    if not result:
        print("開啟成功")
        print("=========================================")
        print("連線網址：http://"+hostname+"/index.php")
        print("登入帳號：admin")
        print("登入密碼：Aa1234567890")
        print("=========================================")
        print("資料庫連線網址")
        print("連線網址：http://"+hostname+"/phpMyAdmin/index.php")
        print("登入帳號：root")
        print("登入密碼：Aa123456789")
    client.close()
    atexit.register(_join_lingering_threads)
    input("按下Enter即可離開....")
except Exception:
    print('Exception!!')
    raise
