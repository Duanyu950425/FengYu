'''
什么是 request 模块？
    Python 中封装好的一个基于网络请求的模块

requests 模块的编码流程
1.指定 url
2.发送请求
3.返回一个响应
4.持久化响应数据

反爬机制：
1.UA 检测：门站通过检测请求载体的身份标识，来判断请求是否是爬虫发起的，如果是，直接返回错误页面
  反反爬机制：UA 伪装
'''
import requests


# 一个简易的网页采集器
def myPachong():
    my_url = "https://www.sogou.com/web"

    # 如果 url 里需要带参数，直接定义一个字典，给 get 请求中给 url 关键字赋值
    my_params = {
        "query": "林锐锋"
    }

    # 如果需要伪装 Headers，定义一个字典，给 get 请求中的 headers 关键字赋值
    my_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }

    response = requests.get(url=my_url, params=my_params, headers=my_headers)
    response.encoding = "utf-8"  # 修改响应数据的编码格式，可以解决乱码
    response_text = response.text  # 获取文本内容
    file_path = f'{my_params.get("query")}.html'
    with open(file_path, "w", encoding="utf8") as f_w:
        f_w.write(response_text)


if __name__ == '__main__':
    myPachong()
