import openpyxl
from openpyxl.worksheet.worksheet import Worksheet

from EAM.config.config import config


def read_excel(file_name,sheet_name="Sheet1"):

    workbook=openpyxl.load_workbook(file_name)  #读取文件名

    sheet: Worksheet =workbook[sheet_name]  # 读取sheet页

    data=list(sheet.values)   #获取sheet内容

    title=data[0]

    rows=data[1:]

    data=[dict(zip(title,row)) for row in rows]

    return data


if __name__ == '__main__':

    # fxpath=r'D:\Python_EAM_API\EAM\test_case\tc_cases.xlsx'

    r=read_excel(config.login_file,'category')
    s=r[7]
    print(s)