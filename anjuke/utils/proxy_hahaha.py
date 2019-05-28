import requests

def proxy_pool():

    proxy_pool_url = 'http://127.0.0.2:5000/random'
    try:
        res = requests.get(proxy_pool_url)
        if res.status_code == 200:       # 也可以不用判断状态码，毕竟是请求自己的电脑，一般请求不会出问题
            return res.text             # 但是一定要确保代理池是运行着的才行

    except ConnectionError:
        return None
