import requests, time
from bs4 import BeautifulSoup
from selenium import webdriver

wating_sec = 0.5

url_Guui_villa = 'https://new.land.naver.com/houses?ms=37.5428535,127.0931897,15&a=VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL' # 구의동, 빌라 주택, 거래방식: 전체
url_Guui_onetworoom = 'https://new.land.naver.com/rooms?ms=37.5434469,127.0924734,15&a=APT:OPST:ABYG:OBYG:GM:OR:VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL&aa=SMALLSPCRENT' # 구의동, 원투룸, 거래방식: 전체
url_Jayang_villa = 'https://new.land.naver.com/houses?ms=37.5344483,127.0831475,15&a=VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL' # 자양동, 빌라 주택, 거래방식: 전체
url_Jayang_onetworoom = 'https://new.land.naver.com/rooms?ms=37.5348716,127.0787405,15&a=APT:OPST:ABYG:OBYG:GM:OR:VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL&aa=SMALLSPCRENT' # 자양동, 원투룸, 거래방식: 전체
url_list = [url_Guui_villa, url_Guui_onetworoom, url_Jayang_villa, url_Jayang_onetworoom]
url_dict = {'구의빌라': url_Guui_villa, '구의원룸': url_Guui_onetworoom, '자양빌라': url_Jayang_villa, '자양원룸':url_Jayang_onetworoom}

driver = webdriver.Chrome()

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

for title in url_dict:
    total_dict = {}
    total_dict_string = ''
    driver.get(url_dict[title])
    driver.find_element_by_link_text("최신순").click()
    time.sleep(wating_sec)

    for i in range(1, 3):
        try: 
            driver.find_element_by_xpath('//*[@id="listContents1"]/div/div/div[1]/div[{}]/div/div[2]/a'.format(i)).click()
        except:
            driver.find_element_by_xpath('//*[@id="listContents1"]/div/div/div[1]/div[{}]/div'.format(i)).click()
    
        time.sleep(wating_sec)
        current_url = driver.current_url

        res = requests.get(current_url, headers=headers)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, 'html5lib')
        
        # print(soup.find(text="아파트"))

        print(soup.find("em", string="분양"))
        print(soup.find("div", attrs={"class":"panel_group"}))

        time.sleep(wating_sec)