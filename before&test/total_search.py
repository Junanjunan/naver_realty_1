import time, smtplib, ssl
from selenium import webdriver
from urllib.parse import urlsplit, parse_qs
# from address import address_set
from address import my_list_dict


wating_sec = 0.5

url_Guui_villa = 'https://new.land.naver.com/houses?ms=37.5428535,127.0931897,15&a=VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL' # 구의동, 빌라 주택, 거래방식: 전체
url_Guui_onetworoom = 'https://new.land.naver.com/rooms?ms=37.5434469,127.0924734,15&a=APT:OPST:ABYG:OBYG:GM:OR:VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL&aa=SMALLSPCRENT' # 구의동, 원투룸, 거래방식: 전체
url_Jayang_villa = 'https://new.land.naver.com/houses?ms=37.5344483,127.0831475,15&a=VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL' # 자양동, 빌라 주택, 거래방식: 전체
url_Jayang_onetworoom = 'https://new.land.naver.com/rooms?ms=37.5348716,127.0787405,15&a=APT:OPST:ABYG:OBYG:GM:OR:VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL&aa=SMALLSPCRENT' # 자양동, 원투룸, 거래방식: 전체
url_list = [url_Guui_villa, url_Guui_onetworoom, url_Jayang_villa, url_Jayang_onetworoom]


driver = webdriver.Chrome()





for url in url_list:
    total_dict = {}
    total_dict_string = ''
    driver.get(url)
    driver.find_element_by_link_text("최신순").click()
    time.sleep(wating_sec)
    
    try:
        for i in range(1, 10000):

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
            # query = urlsplit(current_url).query
            # print(query)
            # params = parse_qs(query)
            # print(params)
            
            # print("-------------")

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




    for i in total_dict:
        f_day = total_dict[i]['광고확인일']
        f_type = total_dict[i]['거래방식']
        f_price = total_dict[i]['가격']
        f_spec = total_dict[i]['특징']
        f_realtor = total_dict[i]['중개사']
        f_url = total_dict[i]['url']
        f_room = total_dict[i]['호실']
        f_phone = total_dict[i]['연락처']

        # total_dict_string += f'{i}, 장부: 호실 - {f_room}, 연락처 - {f_phone} / 네이버:  {f_type}, {f_price}, {f_spec}, {f_realtor} \n'
        # total_dict_string += f'{i}, {f_room}(호), {f_phone}, {f_type}, {f_price}, {f_spec}, {f_realtor} \n'
        total_dict_string += f'{i}, \n{f_day}, \n{f_room}(호), \n{f_phone}, \n{f_type}, \n{f_price}, \n{f_spec}, \n{f_realtor} \n\n'
        # total_dict_string += f_url -- url 전송이 안됨...

    total_dict_string = total_dict_string.encode('utf8')

    print(total_dict_string)

    port = 465
    password = 'mlhwdtmjcvzmugof'

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("taltalmailing@gmail.com", password)
        server.sendmail(
            'taltalmailing@gmail.com', 
            'jjj1305@hanmail.net', 
            total_dict_string)

driver.close()
