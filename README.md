# 自动健康申报脚本

基于selenium编写的东南大学全校师生每日健康申报自动化脚本，解决车友们因忘记申报而无权限卡的痛点。
只需要配置好驱动和python库，简单填写一卡通号即可使用，容易上手！
配合Windows系统的计划任务使用效果更佳。

## 使用说明

需要导入的python库：time、selenium

```
pip install selenium
```

根据**浏览器的种类以及版本号**下载对应的Webdriver驱动程序。

Chrome：http://chromedriver.storage.googleapis.com/index.html

Edge：https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

**代码中需要填写相关信息的地方已经用TODO高亮注释。**

填写浏览器是Edge还是Chrome。

```
browser = 'Edge'
```

把以下函数的参数改成Webdriver驱动程序的绝对路径。

```
service = Service(executable_path=r'D:\edgedriver_win64\msedgedriver.exe')
```

分别填写一卡通号，一卡通密码和申报的体温。**可以填写多份一卡通及密码，以同时为多人打卡**。

```
userid = ['一卡通号1', '一卡通号2', '一卡通号3']
password = ['密码1', '密码2', '密码3']
temp = '36.7'
```

若要显示浏览器界面需注释以下语句。

```
option.add_argument("--headless")
```

自动申报记录`log.txt`保存在和脚本同路径下。

## 设置每日自动运行该脚本

下面简单描述利用Windows系统的计划任务设置设置每日自动运行该脚本的方法。

**右击开始键（Windows徽标）**，选择**计算机管理**，依次打开**系统工具**、**任务计划程序**，在`操作`一栏选择**创建任务**。

在`常规`一栏依次填入**名称**、**描述**，并且**配置**选择**Windows10**。

新建**触发器**，设置**每天**，调整**开始时间**并**确定**。

新建**操作**，**程序或脚本**处填写Python的路径（可在cmd中使用`where Python`或者在Python环境中用`import sys``sys.path`获得）；

**添加参数**填写脚本（.py文件）绝对路径，**起始于**填写脚本的目录，例如：

```
程序或脚本：C:\Users\86177\AppData\Local\Programs\Python\Python39\python.exe
添加参数：D:\Desktop\CODE\py\打卡\daka.py
起始于：D:\Desktop\CODE\py\打卡
```

之后一路点确定并且输入系统账户密码即可设置完成。

PS：SEU-WLAN无论是否选择无感登录，连接一段时间都会要求重新认证，所以大家在使用该脚本时也要留意每日是否成功打卡。推荐结合Python SMTP邮件的方式通知打卡结果。
