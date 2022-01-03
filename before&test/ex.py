from selenium import webdriver
import time
import csv

f = open('부동산빌라주택(11월28일).csv', 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)

title = "확인 주소 거래유형 가격 공인중개사정보".split(" ")
writer.writerow(title)

driver = webdriver.Chrome()
# 자양동 빌라,주택 전체
url_0 = 'https://new.land.naver.com/houses?ms=37.536371,127.0885548,15&a=VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL'
# 구의동 빌라,주택 전체
url_1 = 'https://new.land.naver.com/houses?ms=37.5453654,127.0929933,15&a=VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL'

url_list = [url_0, url_1]

target_day = '20.11.28.'

sec = 0.3
long_sec = 1

def ob_info_func():
    try:
        ob_address = driver.find_element_by_xpath('/html/body/div[2]/div/section/div[2]/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr[1]/td').text
    except:
        ob_address = driver.find_element_by_xpath('/html/body/div[2]/div/section/div[2]/div[2]/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td').text
    ob_type = driver.find_element_by_class_name("info_article_price").find_element_by_class_name("type").text
    ob_price = driver.find_element_by_class_name("info_article_price").find_element_by_class_name("price").text
    try:
        ob_agent = driver.find_element_by_class_name('table_td_agent').text
    except:
        ob_agent = driver.find_element_by_class_name('direct_deals').text
    print(ob_agent)
    print(ob_date)
    print(ob_address)
    print(ob_type)
    print(ob_price)
    ob_info.append(ob_date)
    ob_info.append(ob_address)
    ob_info.append(ob_type)
    ob_info.append(ob_price)
    ob_info.append(ob_agent)

for i in url_list:
    driver.get(i)
    driver.find_element_by_link_text("최신순").click()
    time.sleep(long_sec)

    obs_list = []

    for i in range(1, 100):
        ob_info = []
        if driver.find_element_by_xpath('/html/body/div[2]/div/section/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[{}]/div/div[2]/span/em[2]'.format(i)).text == target_day:
            ob_date = driver.find_element_by_xpath('/html/body/div[2]/div/section/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[{}]/div/div[2]/span/em[2]'.format(i)).text
            try:
                driver.find_element_by_xpath('/html/body/div[2]/div/section/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[{}]/div/div[2]/a'.format(i)).click()
                time.sleep(sec)
                ob_info_func()

            except:
                driver.find_element_by_xpath('/html/body/div[2]/div/section/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[{}]'.format(i)).click()
                time.sleep(sec)
                ob_info_func()
        elif driver.find_element_by_xpath('/html/body/div[2]/div/section/div[2]/div[1]/div/div/div/div[2]/div/div/div/div[{}]/div/div[2]/span/em[2]'.format(i)).text == target_day:
            ob_date = driver.find_element_by_xpath('/html/body/div[2]/div/section/div[2]/div[1]/div/div/div/div[2]/div/div/div/div[{}]/div/div[2]/span/em[2]'.format(i)).text
            try:
                driver.find_element_by_xpath('/html/body/div[2]/div/section/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[{}]/div/div[2]/a'.format(i)).click()
                time.sleep(sec)
                ob_info_func()
            except:
                driver.find_element_by_xpath('/html/body/div[2]/div/section/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[{}]'.format(i)).click()
                time.sleep(sec)
                ob_info_func()
        else:
            break
        
        obs_list.append(ob_info)
        writer.writerow(obs_list[i-1])
    
        flag = driver.find_element_by_xpath('/html/body/div[2]/div/section/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[{}]'.format(i))
        driver.execute_script("arguments[0].scrollIntoView();", flag)  # 내부 스크롤 내리기


