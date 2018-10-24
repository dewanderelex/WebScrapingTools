import requests, bs4, xlsxwriter, time, re
from multiprocessing import Pool
from selenium import webdriver

"""
link = 'https://www.facebook.com/groups/ieltsngocbach/members/'
res = requests.get(link)
soup = bs4.BeautifulSoup(res.text, "html.parser")
print(res.text)
"""

workbook = xlsxwriter.Workbook("FBDATA.xlsx")
worksheet = workbook.add_worksheet()
row = 2
col = 1

def find_Email(link):
    res = requests.get(link)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    dataSpan = soup.find_all("span", {"class" : "_c24 _2ieq"})
    for dataDiv in dataSpan:
        for data in dataDiv:
            try:
                emailMatch = re.findall("\S+@gmail\.com", data.text)
            except:
                pass
    return emailMatch

stringData = open("data.txt", mode = "r")
dataSoup = bs4.BeautifulSoup(stringData, "html.parser")
for targetInfo in dataSoup.find_all("div", {"class" : "_60ri fsl fwb fcb"}):
    col = 1
    worksheet.write(row, col, re.findall(".+\?", targetInfo.select("a")[0].get("href"))[0][:-1])
    worksheet.write(row, col+1, find_Email(re.findall(".+\?", targetInfo.select("a")[0].get("href"))[0][:-1]+"/about"))
    row += 1
workbook.close()

