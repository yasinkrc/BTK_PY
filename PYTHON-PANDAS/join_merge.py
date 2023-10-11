import pandas as pd

# customers = {
#      'CustomerId': [1,2,3,4],
#     'FirstName': ["Ahmet","Ali","Hasan","Canan"],
#     'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
#  }

# orders = {
#      'OrderId': [10,11,12,13],
#      'CustomerId': [1,2,5,7],
#      'OrderDate': ['2010-07-04','2010-08-04','2010-07-07','2012-07-04']
#  }



# df_customers=pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
# df_orders=pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])

# print(df_customers)
# print(df_orders)
# result=pd.merge(df_customers,df_orders,how="inner")
# """ 
#    CustomerId FirstName LastName
# 0           1     Ahmet   Yılmaz
# 1           2       Ali  Korkmaz
# 2           3     Hasan    Çelik
# 3           4     Canan   Toprak
#    OrderId  CustomerId   OrderDate
# 0       10           1  2010-07-04
# 1       11           2  2010-08-04
# 2       12           5  2010-07-07
# 3       13           7  2012-07-04
#    CustomerId FirstName LastName  OrderId   OrderDate
# 0           1     Ahmet   Yılmaz       10  2010-07-04
# 1           2       Ali  Korkmaz       11  2010-08-04

# """
# result=pd.merge(df_customers,df_orders,how="left")
# """ 
# 0           1     Ahmet   Yılmaz
# 1           2       Ali  Korkmaz
# 2           3     Hasan    Çelik
# 3           4     Canan   Toprak
#    OrderId  CustomerId   OrderDate
# 0       10           1  2010-07-04
# 1       11           2  2010-08-04
# 2       12           5  2010-07-07
# 3       13           7  2012-07-04
#    CustomerId FirstName LastName  OrderId   OrderDate
# 0           1     Ahmet   Yılmaz     10.0  2010-07-04
# 1           2       Ali  Korkmaz     11.0  2010-08-04
# 2           3     Hasan    Çelik      NaN         NaN
# 3           4     Canan   Toprak      NaN         NaN
# """
# print(result)
customersA = {
    'CustomerId': [1,2,3,4],
    'FirstName': ["Ahmet","Ali","Hasan","Canan"],
    'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB = {
    'CustomerId': [4,5,6,7],
    'FirstName': ["Yağmur","Çınar","Cengiz","Can"],
    'LastName': ["Bilge","Turan","Yılmaz","Turan"]
}



df_customersA=pd.DataFrame(customersA,columns=["CustomerId","FirstName","LastName"])
df_customersB=pd.DataFrame(customersB,columns=["CustomerId","FirstName","LastName"])

result=pd.concat([df_customersA,df_customersB])

""" 
   CustomerId FirstName LastName
0           1     Ahmet   Yılmaz
1           2       Ali  Korkmaz
2           3     Hasan    Çelik
3           4     Canan   Toprak
0           4    Yağmur    Bilge
1           5     Çınar    Turan
2           6    Cengiz   Yılmaz
3           7       Can    Turan

"""


result=pd.concat([df_customersA,df_customersB],axis=1)
"""  
   CustomerId FirstName LastName  CustomerId FirstName LastName
0           1     Ahmet   Yılmaz           4    Yağmur    Bilge
1           2       Ali  Korkmaz           5     Çınar    Turan
2           3     Hasan    Çelik           6    Cengiz   Yılmaz
3           4     Canan   Toprak           7       Can    Turan
"""
print(result)