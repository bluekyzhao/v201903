import requests

from cookiespool.db import RedisClient

conn = RedisClient('accounts', 'weibo')


def set(account, sep='----'):
    username, password = account.split(sep)
    result = conn.set(username, password)
    print('账号', username, '密码', password)
    print('录入成功' if result else '录入失败')


def scan():
    print('请输入账号密码组, 输入exit退出读入')
    while True:
        account = input()
        if account == 'exit':
            break
        set(account)

    #set('erchua8167867@163.com----CLJobu841In')
    #set('change7816457@163.com----QNSxnz835ep')
    #set('liangc2323@163.com----ZGUzft663X1')


if __name__ == '__main__':
    scan()
