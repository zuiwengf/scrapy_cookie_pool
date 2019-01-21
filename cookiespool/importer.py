import requests

from cookiespool.db import RedisClient

conn = RedisClient('accounts', 'weibo')

def set(account, sep='----'):
    username, password = account.split(sep)
    result = conn.set(username, password)
    print('账号', username, '密码', password)
    print('录入成功' if result else '录入失败或者重复录入')

# cmd下录入cookie
def scan():
    print('请输入账号密码组, 输入exit退出读入')
    while True:
        account = input()
        if account == 'exit':
            break
        set(account)

# 文件配置的方式录入cookie
def scan2():
    for account in open("./account_file.txt"):
        if account == 'exit':
            break
        set(account)


if __name__ == '__main__':
    # scan()
    scan2()