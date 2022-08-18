# 自动健康申报小程序
基于selenium编写的东南大学全校师生每日健康申报自动化脚本，解决车友们因忘记申报而无权限卡的痛点

# 使用说明

需要导入的python库：time、selenium

根据**浏览器的种类以及版本号**下载对应的Webdriver驱动程序。

Chrome：'http://chromedriver.storage.googleapis.com/index.html'

Edge：'https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/'

Firefox：'https://github.com/mozilla/geckodriver/releases'

在脚本的代码中，把以下函数的参数改成Webdriver驱动程序的绝对路径。
'''
service = Service(executable_path=r'D:\edgedriver_win64\msedgedriver.exe')
'''

分别填写一卡通号，一卡通密码和申报的体温。**可以填写多份一卡通及密码，以同时为多人打卡**。
'''
userid = ['一卡通号1', '一卡通号2']
password = ['密码1', '密码2']
temp = '36.7'
'''

若要显示浏览器界面需注释以下语句。
'''
option.add_argument("--headless")
'''

自动申报记录'log.txt'保存在和脚本同路径下。

