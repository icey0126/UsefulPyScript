import xlrd

file = 'feature.xlsx'

def read_excel():
    li=[]
    wb = xlrd.open_workbook(filename=file)
    sheet1 = wb.sheet_by_index(0)
    nrows = sheet1.nrows
    for i in range(1,nrows):
        rows = sheet1.row_values(i)
        li.append(rows)
    print(li)

read_excel()