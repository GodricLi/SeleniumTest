# _*_ coding=utf-8 _*_

import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 将chromedriver驱动放在chrome浏览器安装目录下，指定驱动的绝对路径
# browser = webdriver.Chrome(executable_path=r'D:\Google\Chrome\Application\chromedriver')
# try:
# #     browser.get('http://www.baidu.com')
# #     keyword = browser.find_element_by_id('kw')
# #     keyword.send_keys('Python')
# #     keyword.send_keys(Keys.ENTER)
# #     wait = WebDriverWait(browser, 10)
# #     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
# #     # print(browser.current_url)
# #     # print(browser.get_cookies())
# #     # print(browser.page_source)
# # finally:
# #     browser.close()

# 单个节点
# browser = webdriver.Chrome(executable_path=r'D:\Google\Chrome\Application\chromedriver')
# browser.get('http://www.baidu.com')
# input1 = browser.find_element_by_id('kw')  # 使用属性选择
# input2 = browser.find_element_by_css_selector('#kw')  # 使用css选择
# input3 = browser.find_element_by_xpath('//*[@id="kw"]')  # 使用xpath选择
# print(input1)
# print(input2)
# print(input3)
# browser.close()

# 多个节点，淘宝导航栏条目为例
# browser = webdriver.Chrome(executable_path=r'D:\Google\Chrome\Application\chromedriver')
# browser.get('https://www.taobao.com')
# items = browser.find_elements_by_css_selector('.service-bd li')
# print(items)
# browser.close()

# 2.节点交互
# import time
#
# browser = webdriver.Chrome(executable_path=r'D:\Google\Chrome\Application\chromedriver')
# browser.get('http://www.baidu.com')
# input_word = browser.find_element_by_id('kw')
# input_word.send_keys('apple')
# time.sleep(2)
# input_word.clear()
# input_word.send_keys('cherry')
# button = browser.find_element_by_id('su')
# time.sleep(3)
# button.click()
# browser.close()


# 5.动作链操作
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# import time
#
# browser = webdriver.Chrome(executable_path=r'D:\Google\Chrome\Application\chromedriver')
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# s1 = browser.find_element_by_css_selector('#draggable')
# s2 = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(s1, s2)
# actions.perform()
# time.sleep(2)
# browser.close()

# # 6.模拟JavaScript操作
# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome(executable_path=r'D:\Google\Chrome\Application\chromedriver')
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("OK")')
# time.sleep(3)
# browser.close()

# 7.获取节点信息
# 7.1获取属性
# browser = webdriver.Chrome(executable_path=r'D:\Google\Chrome\Application\chromedriver')
# browser.get('https://www.zhihu.com/explore')
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))
# browser.close()

# 7.2获取文本信息
# browser = webdriver.Chrome(executable_path=r'D:\Google\Chrome\Application\chromedriver')
# browser.get('http://www.baidu.com')
# icons = browser.find_element_by_name('tj_trnews')
# print(icons.text)

# 7.3获取id，位置，标签名，大小
# browser = webdriver.Chrome(executable_path=r'D:\Google\Chrome\Application\chromedriver')
# browser.get('http://www.baidu.com')
# icons = browser.find_element_by_name('tj_trnews')
# print(icons.id)
# print(icons.location)
# print(icons.tag_name)
# print(icons.size)


# 8.切换Frame
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
#
# browser = webdriver.Chrome(executable_path=r'D:\Google\Chrome\Application\chromedriver')
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# try:
#     logo_first = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print("Failed")
# browser.switch_to.parent_frame()  # 切换到父级Frame
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)


# 9.延时等待
# 9.1隐式等待：没有找到继续等待，超时抛出异常
# browser = webdriver.Chrome(executable_path=r'D:\Google\Chrome\Application\chromedriver')
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# que = browser.find_element_by_class_name('zu-top-add-question')
# print(que)

# 9.2显式等待
# browser = webdriver.Chrome(executable_path=r'D:\Google\Chrome\Application\chromedriver')
# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser, 10)
# su = wait.until(EC.presence_of_element_located((By.ID, 'q')))  # 等待条件，节点出现
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))  # 等待条件，按钮可以点击
# print(su, button)


# 10.窗口管理
# browser = webdriver.Chrome(executable_path=r'D:\Google\Chrome\Application\chromedriver')
# browser.get('http://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to.window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(2)
# browser.switch_to.window(browser.window_handles[0])
# browser.get('https://www.zhihu.com/explore')


# 11.异常处理
browser = webdriver.Chrome(executable_path=r'D:\Google\Chrome\Application\chromedriver')
browser.get('http://www.baidu.com')
try:
    browser.find_element_by_class_name('hello')
except TimeoutException:
    print('Time out')
try:
    browser.find_element_by_class_name('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()
