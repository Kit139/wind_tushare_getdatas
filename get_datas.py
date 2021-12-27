# import tushare as ts
# ts.set_token('c2ed081aa3b67b6943570b10feb85dda0828ccc7a4daa0d7c14942a2')
# pro = ts.pro_api()



# #多个股票
# df = ts.pro_bar(ts_code='603088.SH', adj='qfq', start_date='20201002', end_date='20211002')
# print(df)

# import WindPy as w

# # w.start()
# w.isconnected()


import os
import pandas as pd



import tushare as ts
ts.set_token('c2ed081aa3b67b6943570b10feb85dda0828ccc7a4daa0d7c14942a2')
pro = ts.pro_api()

# data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
# print(data)

list = os.listdir('./fenlei/')
for name in list[0:1]:
    df = pd.read_excel('./fenlei/'+name)
    # print(df)
    datas = df['代码'].tolist()[:-2]
    df_datas = pd.DataFrame()
    for data in datas:
        df = ts.pro_bar(ts_code=data, adj='qfq', start_date='20201002', end_date='20211002')
        # print(df)
        df_datas = df_datas.append(df)
    print(df_datas)

# list = os.listdir('./finance_fenlei/')
# for name in list:
#     df = pd.read_excel('./finance_fenlei/'+name)
#     datas = df['代码'].tolist()[:-2]
#     df_datas = pd.DataFrame()
#     for data in datas:
#         df_datas.append(ts.pro_bar(ts_code=data, adj='qfq', start_date='20201002', end_date='20211002'))
#     print(df_datas)