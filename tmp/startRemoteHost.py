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
    print("開啟 Linux 遠端網頁主控台....")
    stdin, stdout, stderr = client.exec_command('systemctl start cockpit')
    result = stdout.readlines()
    if not result:
        print("開啟成功")
        print("連線網址："+hostname+":9090")
        print("登入帳號："+username)
        print("登入密碼："+password)
    client.close()
    atexit.register(_join_lingering_threads)
    input("按下Enter即可離開....")
except Exception:
    print('Exception!!')
    raise
