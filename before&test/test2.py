total_dict = {'서울시 광진구 구의동 241-10': {'거래방식': '전세', '가격': '2억 6,000', '특징': '28/22m², 3/5층, 서향', '중개사': '조은공인중개사사무소', 'url': 'https://new.land.naver.com/rooms?ms=37.5434469,127.0924734,15&a=APT:OPST:ABYG:OBYG:GM:OR:VL:DDDGG:JWJT:SGJT:HOJT&e=RETAIL&aa=SMALLSPCRENT&articleNo=2134606431', '호실': '102', '연락처': '010-3645-4911'}}

print(total_dict['서울시 광진구 구의동 241-10']['가격'])


for i in total_dict:
    print(total_dict[i]['거래방식'])
    print(total_dict[i]['가격'])
    print(total_dict[i]['특징'])
    print(total_dict[i]['중개사'])
    print(total_dict[i]['url'])
    print(total_dict[i]['호실'])
    print(total_dict[i]['연락처'])
