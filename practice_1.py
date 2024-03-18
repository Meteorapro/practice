# 这是第一题的内容

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import sys
import os

# 爬取数据模块
def search_exchange_rate(browser,url,time,money):
    browser.get(url)

    browser.find_element(By.NAME,"erectDate").send_keys(time)
    browser.find_element(By.NAME,"nothing").send_keys(time)
    browser.find_element(By.NAME,"pjname").send_keys(money)
    browser.find_element(By.CLASS_NAME,"invest_t").find_element(By.CLASS_NAME,"search_btn").click()
    # time.sleep(5)
    try:
        price=browser.find_element(By.XPATH,'//*[@class="BOC_main publish"]').text.split('\n')[1].split(' ')[3]
        if price[-1]!='对不起，没有检索结果，请换其他检索词重试！':
            return price
        else:
            return
    except:
        return

# 文件写入模块
def write_data(filename,price):
    if os.path.exists(filename):
        with open(filename,"a") as file:
            file.write("\n"+price)
    else:
        with open(filename,"w") as file:
            file.write("现汇卖出价")
            file.write("\n"+price)
    return

firefox_browser=webdriver.Firefox()
url="https://srh.bankofchina.com/search/whpj/search_cn.jsp"

country_name=["英镑","港币","美元","瑞士法郎","德国马克",
              "法国法郎","新加坡元","丹麦克朗","挪威克朗","日元",
              "加拿大元","澳大利亚元","欧元","澳门元","菲律宾比索",
              "泰国铢","新西兰元","卢布",
              "西班牙比塞塔","意大利里拉","荷兰盾","比利时法郎",
              "芬兰马克","印度卢比","印尼卢比","巴西里亚尔",
              "南非兰特","沙特里亚尔","土耳其里拉"]
country_symbol=["GBP","HKD","USD","CHF","DEM",
              "FRF","SGD","DKK","NOK","JPY",
              "CAD","AUD","EUR","MOP","PHP",
              "THP","NZD","SUR",
              "ESP","ITL","NLG","BEF",
              "FIM","INR","IDR","BRC",
              "ZAR","SAR","TRL"]

parsers=sys.argv
try:
    # print(parsers)
    time=parsers[1][:4]+'-'+parsers[1][4:6]+'-'+parsers[1][6:]
    money=country_name[country_symbol.index(parsers[2])]
    # print(time+money)
    data_filename="result.txt"
    price=search_exchange_rate(firefox_browser,url,time,money)
    if price!=None:
        print(price)
        write_data(data_filename,price)
    else:
        print("无该时间货币数据")
except:
    print("参数输入错误")

firefox_browser.quit()