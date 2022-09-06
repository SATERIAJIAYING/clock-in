# encoding:utf-8
def main():
    import time
    from time import sleep

    # TODO: 一卡通号  密码  体温  尝试次数
    userid = ['一卡通号1', '一卡通号2', '一卡通号3']
    password = ['密码1', '密码2', '密码3']
    temp = '36.7'
    times = 3

    # TODO: 浏览器类型
    browser = 'Edge'

    if browser == 'Edge':
        from selenium.webdriver.edge.service import Service
    elif browser == 'Chrome':
        from selenium.webdriver.chrome.service import Service
    else:
        raise NameError('unsupported browser!')

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys

    # TODO: 浏览器Webdriver绝对路径
    service = Service(executable_path=r'D:\edgedriver_win64\msedgedriver.exe')

    if browser == 'Edge':
        option = webdriver.EdgeOptions()
    else:
        option = webdriver.ChromeOptions()

    # 若要显示浏览器界面需注释以下语句
    # option.add_argument("--headless")

    for numUser in range(len(userid)):
        for numTry in range(times):
            step = 0
            driver = 0
            try:

                if browser == 'Edge':
                    driver = webdriver.Edge(service=service, options=option)
                else:
                    driver = webdriver.Chrome(service=service, options=option)

                driver.get(url=r'http://ehall.seu.edu.cn/new/index.html')
                driver.maximize_window()
                driver.implicitly_wait(10)

                driver.find_element(By.XPATH, '//*[@id="ampHasNoLogin"]/span[1]').click()
                driver.implicitly_wait(10)

                ActionChains(driver)\
                    .send_keys(userid[numUser])\
                    .key_down(Keys.TAB)\
                    .send_keys(password[numUser])\
                    .perform()

                sleep(3)

                driver.find_element(By.XPATH, '//*[@id="xsfw"]').click()
                driver.implicitly_wait(10)

                step += 1   # step == 1
                driver.find_element(By.LINK_TEXT, '全校师生每日健康申报系统').click()
                driver.implicitly_wait(10)
                step += 1

                driver.switch_to.window(driver.window_handles[1])
                step += 1  # step == 3
                driver.find_element(By.XPATH, '/html/body/main/article/section/div[2]/div[1]').click()
                driver.implicitly_wait(10)
                step += 1

                sleep(3)
                step += 1  # step == 5
                temp_input = driver.find_element(By.XPATH, '//*[@id="emapForm"]/div/div[4]/div[2]/div[1]/div[1]')
                driver.implicitly_wait(10)
                step += 1
                ActionChains(driver)\
                    .click(temp_input)\
                    .send_keys(temp)\
                    .key_down(Keys.TAB).key_up(Keys.TAB)\
                    .key_down(Keys.TAB).key_up(Keys.TAB)\
                    .key_down(Keys.TAB).key_up(Keys.TAB)\
                    .key_down(Keys.TAB).key_up(Keys.TAB)\
                    .key_down(Keys.TAB).key_up(Keys.TAB)\
                    .perform()

                driver.find_element(By.XPATH, '// *[ @ id = "save"]').click()
                driver.implicitly_wait(10)

                sleep(2)
                driver.find_element(By.XPATH, '/html/body/div[62]/div[1]/div[1]/div[2]/div[2]/a[1]').click()
                driver.implicitly_wait(10)

                print('**', driver.title, '**', sep='')

                notice = '一卡通号' + userid[numUser] + '已于' + time.strftime('%m月%d日%H：%M完成当日健康打卡\n')
                print(notice)
                with open(file='log.txt', mode='a') as file:
                    file.write(notice)

                # 若注释，完成脚本后不会关闭浏览器
                driver.quit()
                break

            except Exception as r:
                print('Error:', r, error_type(step, userid[numUser]))
                with open(file='log.txt', mode='a') as file:
                    file.write('Error!' + r.__str__() + error_type(step, userid[numUser]) + time.strftime(' %m-%d %H:%M\n'))
                numTry += 1
                # 若注释，完成脚本后不会关闭浏览器
                driver.quit()


def error_type(step, userid) -> str:
    if step == 1:
        return '\n{}:一卡通号或密码错误！'.format(userid)
    elif step == 5:
        return '\n{}:不在规定的打卡时间内,或者当日已经完成健康申报，不能重复申报！'.format(userid)
    else:
        return ''


if __name__ == '__main__':
    main()
