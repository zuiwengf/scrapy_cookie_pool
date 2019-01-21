# CookiesPool

可扩展的Cookies池，目前对接了新浪微博，[m.weibo.cn](https://m.weibo.cn)，可自行扩展其他站点


## 安装

```
pip3 install -r requirements.txt
```

## 基础配置 

### 接口基本配置

```python
# Redis数据库地址
REDIS_HOST = 'localhost'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = 'lxh123'

# 产生器使用的浏览器
BROWSER_TYPE = 'Chrome'

# 产生器类，如扩展其他站点，请在此配置
GENERATOR_MAP = {
    'weibo': 'WeiboCookiesGenerator'
}

# 测试类，如扩展其他站点，请在此配置
TESTER_MAP = {
    'weibo': 'WeiboValidTester'
}

# 检测器检测接口
TEST_URL_MAP = {
    'weibo': 'https://m.weibo.cn/api/container/getIndex?uid=1804544030&type=uid&page=1&containerid=1076031804544030'
}

# 产生器和验证器循环周期
CYCLE = 120

# API地址和端口
API_HOST = '127.0.0.1'
API_PORT = 5005

```

### 进程开关

在config.py修改

```python
# 产生器开关，模拟登录添加Cookies
GENERATOR_PROCESS = True
# 验证器开关，循环检测数据库中Cookies是否可用，不可用删除
VALID_PROCESS = True
# API接口服务
API_PROCESS = True
```


## 账号购买

账号可在淘宝购买


## 导入账号

```
python3 importer.py
```

```
请输入账号密码组, 输入exit退出读入
18459748505----astvar3647
14760253606----gmidy8470
14760253607----uoyuic8427
18459749258----rktfye8937
账号 18459748505 密码 astvar3647
录入成功
账号 14760253606 密码 gmidy8470
录入成功
账号 14760253607 密码 uoyuic8427
录入成功
账号 18459749258 密码 rktfye8937
录入成功
exit
```


## 运行

请先导入一部分账号之后再运行，运行命令：

```
python3 run.py
```

## 运行效果

三个进程全部开启：


```
API接口开始运行
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
Cookies生成进程开始运行
Cookies检测进程开始运行
正在生成Cookies 账号 14747223314 密码 asdf1129
正在测试Cookies 用户名 14747219309
Cookies有效 14747219309
正在测试Cookies 用户名 14740626332
Cookies有效 14740626332
正在测试Cookies 用户名 14740691419
Cookies有效 14740691419
正在测试Cookies 用户名 14740618009
Cookies有效 14740618009
正在测试Cookies 用户名 14747222472
Cookies有效 14747222472
Cookies检测完成
验证码位置 420 580 384 544
成功匹配
拖动顺序 [1, 4, 2, 3]
成功获取到Cookies {'SUHB': '08J77UIj4w5n_T', 'SCF': 'AimcUCUVvHjswSBmTswKh0g4kNj4K7_U9k57YzxbqFt4SFBhXq3Lx4YSNO9VuBV841BMHFIaH4ipnfqZnK7W6Qs.', 'SSOLoginState': '1501439488', '_T_WM': '99b7d656220aeb9207b5db97743adc02', 'M_WEIBOCN_PARAMS': 'uicode%3D20000174', 'SUB': '_2A250elZQDeRhGeBM6VAR8ifEzTuIHXVXhXoYrDV6PUJbkdBeLXTxkW17ZoYhhJ92N_RGCjmHpfv9TB8OJQ..'}
成功保存Cookies
```


备注：自己的理解

①录入account
方式一：cmd运行importer.py，通过18459748505----astvar3647的格式输入账号和密码，然后该方法通过调用db.RedisClient类将账号存存储到reids（未设置db库，默认为0，type=hash,key="accounts:weibo"）
方式二：将importer.py的scan修改成scan2，这样的话会读取account_file中的账号，存储到redis
注意：格式都为 account----password；  可以自行设置key值

②api为一个小的falsk网页，配置了一些路由  127.0.0.1:5005
/ 主页，显示 Welcome to Cookie Pool System
/<website>/random  随机获取该网站的一个cookie值    #website为在configs中配置的
/<website>/add/<username>/<password>   #添加账号
/<website>/count   #获取cookie个数

③录入完账号后即可运行run.py主程序，通过函数api启动falsk；通过generate_cookie、valid_cookie和valid_cookie对cookie进行判断保留有效的cookie；

④cookie检验间隔时间在config中设置CYCLE=120秒