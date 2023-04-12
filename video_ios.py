import time
import subprocess
from wda import Client
import wda
# Replace "http://localhost:8100" with the URL of your device

def start_video():
    client = Client("http://localhost:8100")
    client.wait_ready(timeout=15, noprint=True)
    client.app_launch("com.apple.camera")

# client.xpath('//Window/Other[1]/Other[1]/Other[1]/Other[3]/Other[1]/Other[4]').click()
# client.click(0.5, 0.791)
    time.sleep(0.5)
    # client.swipe(0.49, 0.793, 0.351, 0.793, duration=0.5)
    client.swipe(0.498, 0.848,0.34, 0.845, duration=0.5)
    time.sleep(0.5)
    client(label="录制视频").click()
def end_video():
    client = Client("http://localhost:8100")
    client.wait_ready(timeout=15, noprint=True)
    client.app_launch("com.apple.camera")
    # client.click(0.496, 0.871)
    client.click(0.498, 0.922)
def kill_course():
    a = subprocess.Popen('pgrep iproxy',shell=True,stdout=subprocess.PIPE)
    a.wait()
    b = eval(a.stdout.read())
    time.sleep(2)
    subprocess.Popen('kill -9 {}'.format(b),shell=True)
    print('PID为{}的进程已关闭'.format(b))

# def login_1():
#     a = client.xpath('//ScrollView/Other[1]/Other[1]').get()
#     a.set_text('アカウント')
#     client(label="清除文本").click()
#     a.set_text('18348336255')
#     client.xpath('//ScrollView/Button[2]').click()
#     try:
#         client(label="帐号密码登录").click()
#         print('登录中。。。')
#     except wda.exceptions.WDAElementNotFoundError as msg:
#         print("网络超时%s" % msg)
#         client.session().app_terminate("com.baidu.baiduhi")
#         login_1()
#     b = client.xpath('//SecureTextField').get()
#     b.set_text('19980808lkY')
#     client.xpath('//*[@label="文章"]/Other[3]/Button[1]').click()
#     try:
#         client(label="登 录").click()
#         print('登录成功')
#     except wda.exceptions.WDAElementNotFoundError as msg:
#         print("网络超时%s" % msg)
#         client.session().app_terminate("com.baidu.baiduhi")
#         login_1()
#     client.xpath('//NavigationBar/Other[1]/Other[1]/Image[1]').click()
#     client.xpath(
#         '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[1]/Other[1]').click()
#     client.xpath('//ScrollView/Button[1]/StaticText[1]').click()
#     client.xpath('//Alert/Other[1]/Other[1]/Other[2]/ScrollView[2]/Other[1]/Other[1]/Other[3]').click()
#     client.sleep(5)
#     client.session().app_terminate("com.baidu.baiduhi")


# client.xpath('//*[@label="文章"]/Button[1]').click()
#
# try:
#     client(label="帐号密码登录").click()
#     print('登录成功')
# except wda.exceptions.WDAElementNotFoundError as msg:
#     print("失败，查找元素异常%s" % msg)
#     client.session().app_terminate("com.baidu.baiduhi")
# print('*' * 50)
# client.sleep(3)
# ele_1 = client.xpath('//SecureTextField').get()
# ele_1.set_text('19980808lkY')
# client(label="登 录").click()


# def login_2():
#     if client(label="+86").exists:
#         client.click(0.063, 0.064)
#         login_1()
#     else:
#         login_1()


# login_2()
start_video()
time.sleep(5)
end_video()
time.sleep(1)
kill_course()