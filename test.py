import time, smtplib, ssl
from selenium import webdriver





wating_sec = 0.5

url_Guui_villa = 'https://new.land.naver.com/houses?ms=37.5428535,127.0931897,15&a=VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL' # 구의동, 빌라 주택, 거래방식: 전체
url_Guui_onetworoom = 'https://new.land.naver.com/rooms?ms=37.5434469,127.0924734,15&a=APT:OPST:ABYG:OBYG:GM:OR:VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL&aa=SMALLSPCRENT' # 구의동, 원투룸, 거래방식: 전체
url_Jayang_villa = 'https://new.land.naver.com/houses?ms=37.5344483,127.0831475,15&a=VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL' # 자양동, 빌라 주택, 거래방식: 전체
url_Jayang_onetworoom = 'https://new.land.naver.com/rooms?ms=37.5348716,127.0787405,15&a=APT:OPST:ABYG:OBYG:GM:OR:VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL&aa=SMALLSPCRENT' # 자양동, 원투룸, 거래방식: 전체
url_list = [url_Guui_villa, url_Guui_onetworoom, url_Jayang_villa, url_Jayang_onetworoom]


driver = webdriver.Chrome()
# driver.maximize_window()

naver_list = []
my_list = ['서울시 광진구 구의동 80-53', '구의동 221-35']

for url in url_list:
    driver.get(url)
    driver.find_element_by_link_text("최신순").click()
    time.sleep(wating_sec)
    
    for i in range(1, 5):
        try: 
            driver.find_element_by_xpath('//*[@id="listContents1"]/div/div/div[1]/div[{}]/div/div[2]/a'.format(i)).click()
        except:
            driver.find_element_by_xpath('//*[@id="listContents1"]/div/div/div[1]/div[{}]/div'.format(i)).click()
        time.sleep(wating_sec)
        print(driver.find_element_by_xpath('//*[@id="detailContents1"]/div[1]/table/tbody/tr[1]/td').text)
        naver_list.append(driver.find_element_by_xpath('//*[@id="detailContents1"]/div[1]/table/tbody/tr[1]/td').text)
        flag = driver.find_element_by_xpath('/html/body/div[2]/div/section/div[2]/div[1]/div/div[2]/div/div[2]/div/div/div[1]/div[{}]'.format(i))
        driver.execute_script("arguments[0].scrollIntoView();", flag)
        time.sleep(wating_sec)
        print(naver_list)

naver_list_string = ''


for i in naver_list:
    if (i in my_list):
        print(i, " exists")
        naver_list_string += str(i)+","


naver_list_string = naver_list_string.encode('utf8')


port = 465
password = 'mlhwdtmjcvzmugof'

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("taltalmailing@gmail.com", password)
    server.sendmail(
        'taltalmailing@gmail.com', 
        'jjj1305@hanmail.net', 
        naver_list_string)