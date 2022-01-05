import time, datetime, yagmail
import pandas as pd
from selenium import webdriver
from address import my_list_dict


waiting_sec = 0.5
long_waiting_sec = 3

target_day = datetime.date.today().strftime('%y.%m.%d.')

url_Guui_villa = 'https://new.land.naver.com/houses?ms=37.5428535,127.0931897,15&a=VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL' # 구의동, 빌라 주택, 거래방식: 전체
url_Guui_onetworoom = 'https://new.land.naver.com/rooms?ms=37.5434469,127.0924734,15&a=APT:OPST:ABYG:OBYG:GM:OR:VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL&aa=SMALLSPCRENT' # 구의동, 원투룸, 거래방식: 전체
url_Jayang_villa = 'https://new.land.naver.com/houses?ms=37.5344483,127.0831475,15&a=VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL' # 자양동, 빌라 주택, 거래방식: 전체
url_Jayang_onetworoom = 'https://new.land.naver.com/rooms?ms=37.5348716,127.0787405,15&a=APT:OPST:ABYG:OBYG:GM:OR:VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL&aa=SMALLSPCRENT' # 자양동, 원투룸, 거래방식: 전체
url_list = [url_Guui_villa, url_Guui_onetworoom, url_Jayang_villa, url_Jayang_onetworoom]
url_dict = {
    # '구의빌라': url_Guui_villa, 
    # '구의원룸': url_Guui_onetworoom, 
    '자양빌라': url_Jayang_villa, 
    '자양원룸':url_Jayang_onetworoom
    }

driver = webdriver.Chrome()

for url in url_dict:
    total_dict = {}
    total_dict_all = {}
    driver.get(url_dict[url])
    time.sleep(long_waiting_sec)
    driver.find_element_by_link_text("최신순").click()
    time.sleep(long_waiting_sec)
    
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

                time.sleep(waiting_sec)

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
                
                total_dict_all.update(naver_list_dict)

                flag = driver.find_element_by_xpath('/html/body/div[2]/div/section/div[2]/div[1]/div/div[2]/div/div[2]/div/div/div[1]/div[{}]'.format(i))
                driver.execute_script("arguments[0].scrollIntoView();", flag)

                time.sleep(waiting_sec)
    except Exception as e:
        print("-"*50)
        print(e)
        print("-"*50)
        pass

    df1 = pd.DataFrame([
        {
            '주소': 'address', 
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
                'url': '=HYPERLINK("{}", "{}")'.format(total_dict[i]['url'], i),
                '호실': total_dict[i]['호실'],
                '연락처': total_dict[i]['연락처'],
            }
        ])
        
        df1 = df1.append(df2)
    
    df1.to_excel('{}-{}.xlsx'.format(url, datetime.date.today()))

    df3 = pd.DataFrame([
        {
            '주소': 'address', 
            '광고확인일':'update', 
            '거래방식':'type', 
            '가격':'price', 
            '특징':'spec', 
            '중개사': 'agent', 
            'url': 'url'
        }
    ])

    for i in total_dict_all:
        df4 = pd.DataFrame([
            {
                '주소': i,
                '광고확인일': total_dict_all[i]['광고확인일'],
                '거래방식': total_dict_all[i]['거래방식'],
                '가격': total_dict_all[i]['가격'],
                '특징': total_dict_all[i]['특징'],
                '중개사': total_dict_all[i]['중개사'],
                'url': '=HYPERLINK("{}", "{}")'.format(total_dict_all[i]['url'], i)
            }
        ])

        df3 = df3.append(df4)

    df3.to_excel('전체 {}-{}.xlsx'.format(url, datetime.date.today()))
    
    time.sleep(long_waiting_sec)


guui_villa = pd.read_excel('구의빌라-{}.xlsx'.format(datetime.date.today()))
guui_oneroom = pd.read_excel('구의원룸-{}.xlsx'.format(datetime.date.today()))
jayang_villa = pd.read_excel('자양빌라-{}.xlsx'.format(datetime.date.today()))
jayang_oneroom = pd.read_excel('자양원룸-{}.xlsx'.format(datetime.date.today()))


""" mailing """

sender = 'taltalmailing@gmail.com'
password = 'mlhwdtmjcvzmugof'
receiver = 'jjj1305@hanmail.net'
subject = '네이버매물-{}'.format(datetime.date.today())
body = '{} 네이버 매물 정리'.format(datetime.date.today())
filename1 = '구의빌라-{}.xlsx'.format(datetime.date.today())
filename2 = '구의원룸-{}.xlsx'.format(datetime.date.today())
filename3 = '자양빌라-{}.xlsx'.format(datetime.date.today())
filename4 = '자양원룸-{}.xlsx'.format(datetime.date.today())
filename5 = '전체 구의빌라-{}.xlsx'.format(datetime.date.today())
filename6 = '전체 구의원룸-{}.xlsx'.format(datetime.date.today())
filename7 = '전체 자양빌라-{}.xlsx'.format(datetime.date.today())
filename8 = '전체 자양원룸-{}.xlsx'.format(datetime.date.today())
filelist = [filename1, filename2, filename3, filename4, filename5, filename6, filename7, filename8]


yag = yagmail.SMTP(sender, password)
yag.send(
    to=receiver,
    subject=subject,
    contents=body, 
    attachments=filelist
)


