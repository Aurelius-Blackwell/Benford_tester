import math
from scipy import stats
import openpyxl

doc = 'benfordTests_copy.xlsx'
wb = openpyxl.load_workbook(doc)
sheet = wb['sheetname']

row = 4
for i in range(row, sheet.max_row):
    print(sheet['a'+str(row)].value)
    #set y variable
    y = []
    for cellObj in sheet['c'+str(row):'k'+str(row)]:
        for i in cellObj:
            y.append(i.value)
    #set x variable
    x = []
    for i in range(1,10):
        x.append(math.log10((1+i)/i))
    slope, intercept, r, p, std_err = stats.linregress(x, y)
    sheet['o'+str(row)].value = float(slope)
    sheet['p'+str(row)].value = float(intercept)
    sheet['q'+str(row)].value = float(r)
    sheet['r'+str(row)].value = float(p)
    sheet['s'+str(row)].value = float(std_err)
    wb.save('benfordTests_second_copy.xlsx')
    row +=1

wb.close()
