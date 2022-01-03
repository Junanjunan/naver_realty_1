x = {
        'a': {'address':'768-1', 'owner':'mom'}, 
        'b': {'address':'251-127', 'owner':'me'}
    }


y = {
    'a': {'color':'red', 'phone': '010'},
    'b': {'color':'blue', 'phone': '02'}
}


naver_list = {
    'address': {'price':'100', 'deposit-fee':'1000/60', 'f/f':'3/5', 'room/toilet': '1/1'}
}

my_list = {
    'address': {'phone': '010-'}
}

naver_list_address = naver_list.get('address')
my_list_address = my_list.get('address')

print(naver_list_address)
print("---")
print(my_list_address)

naver_list_address.update(my_list_address)

print("-----------")
print(naver_list_address)

