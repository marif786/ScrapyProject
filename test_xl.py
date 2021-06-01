# # # Program extracting all columns
# # # name in Python
# # import xlrd
# # web = 'https://www.dallascad.org/DeletedAcct.aspx?ID='
# #
# # loc = '/Users/ARK/Desktop/test.xlsx'
# #
# # wb = xlrd.open_workbook(loc)
# # sheet = wb.sheet_by_index(0)
# # sheet.cell_value(0, 0)
# #
# # for i in range(sheet.nrows):
# #     print(web+sheet.cell_value(i, 0))
# # #
# from openpyxl import load_workbook
#
# # Start by opening the spreadsheet and selecting the main sheet
# workbook = load_workbook(filename="/Users/ARK/Desktop/output.xlsx")
# sheet = workbook.active
#
# # Write what you want into a specific cell
# i=1
# while(i<50):
#     index = "B" + repr(i)
#     print(index)
#     sheet["B"+repr(i)] = "Reading"
#     i+=1
# # Save the spreadsheet
# workbook.save(filename="/Users/ARK/Desktop/output.xlsx")
#
#
#
import re
import urllib
from bs4 import BeautifulSoup

# page  = "https://www.dallasact.com/act_webdev/dallas/showdetail2.jsp?can=00000408685000000&ownerno=0"
#
# soup = BeautifulSoup(page, 'html.parser')
# text=soup.find('b', text='Address:')
# print(text)
import requests
from bs4 import BeautifulSoup,Tag
import re
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

url = "https://www.dallasact.com/act_webdev/dallas/showdetail2.jsp?can=00000408685000000&ownerno=0"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
# print(soup.prettify())
text=soup.find('h3').get_text()
print(text)
print(soup.find("Address:"))
add = soup.find("h3").get_text()
print(add)


#
# for x in text.findAllNext('ul'):
#     print (x.li.b.string,",")
#
# text=soup.find('h3', text='Address:')
#
# for x in text.findAllNext('ul'):
#     print(x.li.b.string,",")