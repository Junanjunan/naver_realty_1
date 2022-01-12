import time, datetime, yagmail
import pandas as pd
from selenium import webdriver
from urllib import parse
from address import my_list_dict
from url_dict import url_dict


waiting_sec = 0.5
long_waiting_sec = 3

today = datetime.date.today()
days = 3
target_day = today - datetime.timedelta(days=days)
date_range = pd.date_range(start = target_day, end = today)


day_list = []
for i in range(0, days+1):
    day_list.append(date_range[i].strftime('%y.%m.%d.'))


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
            if driver.find_element_by_xpath('//*[@id="listContents1"]/div/div/div[1]/div[{}]/div/div[2]/span/em[2]'.format(i)).text in day_list:
            # if True:

                parse_result = parse.urlparse(url_dict[url])
                query_dict = parse.parse_qs(parse_result.query)

                if 'ae' in query_dict.keys():
                    if query_dict['ae'] == ['ONEROOM']:
                        room = 1
                    else:
                        room = 2
                elif 'q' in query_dict.keys():
                    if query_dict['q'] == ['ONEROOM']:
                        room = 1
                    elif query_dict['q'] == ['TWOROOM']:
                        room = 2
                    elif query_dict['q'] == ['THREEROOM']:
                        room = 3
                    else:
                        room = 4
                else:
                    room = '.'

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
                
                naver_list_dict = {address: {'광고확인일':day, '거래방식':type, '가격':price, '방수':room, '특징': spec, '중개사': realtor, 'url': current_url}}

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
    
    df_excel = pd.DataFrame([
            {
                '주소': 'address', 
                '광고확인일':'update', 
                '거래방식':'type', 
                '가격':'price',
                '방수':'room', 
                '특징':'spec', 
                '중개사': 'agent', 
                '호실':'hosil', 
                '연락처':'phone',
                'url': 'url',
            }
        ])

    naver_excel = pd.DataFrame([
            {
                '주소': 'address', 
                '광고확인일':'update', 
                '거래방식':'type', 
                '가격':'price',
                '방수':'room', 
                '특징':'spec', 
                '중개사': 'agent',
                'url': 'url',
            }
        ])    

    df1 = df_excel
    
    for i in total_dict:
        df2 = pd.DataFrame([
            {
                '주소': i,
                '광고확인일': total_dict[i]['광고확인일'],
                '거래방식': total_dict[i]['거래방식'],
                '가격': total_dict[i]['가격'],
                '방수': total_dict[i]['방수'],
                '특징': total_dict[i]['특징'],
                '중개사': total_dict[i]['중개사'],
                '호실': total_dict[i]['호실'],
                '연락처': total_dict[i]['연락처'],
                # 'url': '=HYPERLINK("{}", "{}")'.format(total_dict[i]['url'], i),
                'url': total_dict[i]['url'],
            }
        ])
        
        df1 = df1.append(df2)
    
    df1.to_excel('{}-{}.xlsx'.format(url, datetime.date.today()))

    df3 = naver_excel

    for i in total_dict_all:
        df4 = pd.DataFrame([
            {
                '주소': i,
                '광고확인일': total_dict_all[i]['광고확인일'],
                '거래방식': total_dict_all[i]['거래방식'],
                '가격': total_dict_all[i]['가격'],
                '방수': total_dict_all[i]['방수'],
                '특징': total_dict_all[i]['특징'],
                '중개사': total_dict_all[i]['중개사'],
                # 'url': '=HYPERLINK("{}", "{}")'.format(total_dict_all[i]['url'], i)
                'url': total_dict_all[i]['url']
            }
        ])

        df3 = df3.append(df4)

    df3.to_excel('전체 {}-{}.xlsx'.format(url, datetime.date.today()))
    
    time.sleep(long_waiting_sec)


file_list = []
naver_list = []
for url in url_dict:
    read_excel = pd.read_excel('{}-{}.xlsx'.format(url, datetime.date.today()))
    read_excel.drop([0], inplace=True)
    df_excel = df_excel.append(read_excel)

    naver_read_excel = pd.read_excel('전체 {}-{}.xlsx'.format(url, datetime.date.today()))
    naver_read_excel.drop([0], inplace=True)
    naver_excel = naver_excel.append(naver_read_excel)

    file_list.append('{}-{}.xlsx'.format(url, datetime.date.today()))
    file_list.append('전체 {}-{}.xlsx'.format(url, datetime.date.today()))


df_excel.to_excel('전번매물통합-{}.xlsx'.format(datetime.date.today()))
naver_excel.to_excel('네이버매물통합-{}.xlsx'.format(datetime.date.today()))

file_list.append('전번매물통합-{}.xlsx'.format(datetime.date.today()))
file_list.append('네이버매물통합-{}.xlsx'.format(datetime.date.today()))

""" mailing """

sender = 'taltalmailing@gmail.com'
password = 'mlhwdtmjcvzmugof'
receiver = 'jjj1305@hanmail.net'
subject = '네이버매물-{}'.format(datetime.date.today())
body = '{} 네이버 매물 정리'.format(datetime.date.today())

yag = yagmail.SMTP(sender, password)
yag.send(
    to=receiver,
    subject=subject,
    contents=body, 
    attachments=file_list
)


