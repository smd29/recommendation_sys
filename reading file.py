import xlrd
import numpy as np
import pandas as pd
from pandas import DataFrame

#loc=r"C:\Users\nEW u\Desktop\User_rating_dataset.xls"
loc =r"C:\Users\nEW u\Desktop\housing_dataset.xlsx"

# # To open Workbook
# wb = xlrd.open_workbook(loc)
# #wb.head()
# sheet = wb.sheet_by_index(0)
# print(type(sheet))
# # For row 0 and column 0
# print(sheet.cell_value(0, 0))
# row_count = sheet.nrows #header includedd
# #print(type(row_count))
# #row_count=str(row_count)
# #print("Total users: "+str(row_count))
# column_count = sheet.ncols
# #print(column_count)
# #i=1
# plot=[]
# #for i in range(1,column_count):
#     #print(sheet.row_values(i))
#     #plot[i]=sheet.row_values(i)
#     #plot.append(plot)
# print(wb[1:column_count])
xls = pd.ExcelFile(loc)
sheetX = xls.parse(0) #1 is the sheet number    #0 being the first sheet
# var1 = sheetX['User ID']
# var2 = sheetX['Price']
# var3 = sheetX['Location']
# var4 = sheetX['Mode_of_Sharing']
# var5 = sheetX['Flat_type']

#attributes = pd.read_excel(loc,header=None)
#attributes = sheetX.head(1)
#print(attributes)
#print(df.loc)




