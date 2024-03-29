import time, datetime, smtplib, ssl
import pandas as pd
from selenium import webdriver
from address import my_list_dict


print(datetime.datetime.now())

wating_sec = 0.5

target_day = '21.12.31.'

url_Guui_villa = 'https://new.land.naver.com/houses?ms=37.5428535,127.0931897,15&a=VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL' # 구의동, 빌라 주택, 거래방식: 전체
url_Guui_onetworoom = 'https://new.land.naver.com/rooms?ms=37.5434469,127.0924734,15&a=APT:OPST:ABYG:OBYG:GM:OR:VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL&aa=SMALLSPCRENT' # 구의동, 원투룸, 거래방식: 전체
url_Jayang_villa = 'https://new.land.naver.com/houses?ms=37.5344483,127.0831475,15&a=VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL' # 자양동, 빌라 주택, 거래방식: 전체
url_Jayang_onetworoom = 'https://new.land.naver.com/rooms?ms=37.5348716,127.0787405,15&a=APT:OPST:ABYG:OBYG:GM:OR:VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL&aa=SMALLSPCRENT' # 자양동, 원투룸, 거래방식: 전체
url_list = [url_Guui_villa, url_Guui_onetworoom, url_Jayang_villa, url_Jayang_onetworoom]
url_dict = {'구의빌라': url_Guui_villa, '구의원룸': url_Guui_onetworoom, '자양빌라': url_Jayang_villa, '자양원룸':url_Jayang_onetworoom}

driver = webdriver.Chrome()



for url in url_dict:
    total_dict = {}
    total_dict_string = ''
    driver.get(url_dict[url])
    driver.find_element_by_link_text("최신순").click()
    time.sleep(wating_sec)
    
    try:
        for i in range(1, 10000):
            # if driver.find_element_by_xpath('//*[@id="listContents1"]/div/div/div[1]/div[{}]/div/div[2]/span/em[2]'.format(i)).text == target_day:
            if True:
                try:
                    realtor = driver.find_element_by_xpath('//*[@id="listContents1"]/div/div/div[1]/div[{}]/div/div[1]/div/span[2]/a'.format(i)).text
                except:
                    realtor = driver.find_element_by_xpath('//*[@id="listContents1"]/div/div/div[1]/div[{}]/div/div[1]/div/span[2]/span'.format(i)).text

                

                try: 
                    driver.find_element_by_xpath('//*[@id="listContents1"]/div/div/div[1]/div[{}]/div/div[2]/a'.format(i)).click()
                except:
                    driver.find_element_by_xpath('//*[@id="listContents1"]/div/div/div[1]/div[{}]/div'.format(i)).click()
                time.sleep(wating_sec)
                current_url = driver.current_url


                day = driver.find_element_by_xpath('//*[@id="listContents1"]/div/div/div[1]/div[{}]/div/div[2]/span/em[2]'.format(i)).text

                try:
                    spec = driver.find_element_by_xpath('//*[@id="listContents1"]/div/div/div[1]/div[{}]/div/a/div[3]/p[1]/span'.format(i)).text        # 사진 없는 경우
                except:
                    spec = driver.find_element_by_xpath('//*[@id="listContents1"]/div/div/div[1]/div[{}]/div/a[2]/div[3]/p[1]/span'.format(i)).text     # 사진 있는 경우

                type = driver.find_element_by_class_name('info_article_price').find_element_by_class_name('type').text

                price = driver.find_element_by_class_name('info_article_price').find_element_by_class_name('price').text

                address = driver.find_element_by_xpath('//*[@id="detailContents1"]/div[1]/table/tbody/tr[1]/td').text

                
                naver_list_dict = {address: {'광고확인일':day, '거래방식':type, '가격':price, '특징': spec, '중개사': realtor, 'url': current_url}}


                if (address in my_list_dict) and (naver_list_dict[address]['중개사'] != '연세공인중개사사무소'):
                    my_list_address = my_list_dict.get(address)
                    naver_list_dict[address].update(my_list_address)
                    total_dict.update(naver_list_dict)

                    print(total_dict)


                flag = driver.find_element_by_xpath('/html/body/div[2]/div/section/div[2]/div[1]/div/div[2]/div/div[2]/div/div/div[1]/div[{}]'.format(i))
                driver.execute_script("arguments[0].scrollIntoView();", flag)

                time.sleep(wating_sec)
    except:
        pass

    print("-"*100)
    print(total_dict)

     
    df1 = pd.DataFrame([
        {'주소': 'address', 
         '광고확인일':'update', 
         '거래방식':'type', 
         '가격':'price', 
         '특징':'spec', 
         '중개사': 'agent', 
         'url': 'url', 
         '호실':'hosil', 
         '연락처':'phone'
         }
    ])
    
    for i in total_dict:
        df2 = pd.DataFrame([
            {
                '주소': i,
                '광고확인일': total_dict[i]['광고확인일'],
                '거래방식': total_dict[i]['거래방식'],
                '가격': total_dict[i]['가격'],
                '특징': total_dict[i]['특징'],
                '중개사': total_dict[i]['중개사'],
                'url': total_dict[i]['url'],
                '호실': total_dict[i]['호실'],
                '연락처': total_dict[i]['연락처'],
            }
        ])
        
        df1 = df1.append(df2)
    
    df1.to_excel('{}.xlsx'.format(url))

driver.close()
