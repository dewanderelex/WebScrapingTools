import requests, bs4, xlsxwriter, time, re
from multiprocessing import Pool
from selenium import webdriver

"""
link = 'https://www.facebook.com/groups/ieltsngocbach/members/'
res = requests.get(link)
soup = bs4.BeautifulSoup(res.text, "html.parser")
print(res.text)
"""
"""
workbook = xlsxwriter.Workbook("FBDATA.xlsx")
worksheet = workbook.add_worksheet()
row = 2
col = 1
"""

#form_data = {"email" : "dungnv.edu@gmail.com", "password" : "Vityeulon123!@#"}
#res = requests.get("https://www.facebook.com/eddrda/about")
driver = webdriver.PhantomJS(executable_path='C:\\Program Files\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
driver.get('https://www.facebook.com/eddrda/about')
res = driver.execute_script("return document.documentElement.innerHTML;")
soup = bs4.BeautifulSoup(res, "html.parser")
dataSpan = soup.find_all("span", {"class" : "_c24 _2ieq"})
found = False
emailMatch = []
for dataDiv in dataSpan:
    for data in dataDiv:
        emailMatch = re.findall("\S+@gmail\.com", data.text)
        if emailMatch != []:
            found = True
            break
    if found:
        break


print(emailMatch)

"""
stringData = open("data.txt", mode = "r")
dataSoup = bs4.BeautifulSoup(stringData, "html.parser")
for targetInfo in dataSoup.find_all("div", {"class" : "_60ri fsl fwb fcb"}):
    col = 1
    worksheet.write(row, col, re.findall(".+\?", targetInfo.select("a")[0].get("href"))[0][:-1])
    worksheet.write(row, col+1, find_Email(re.findall(".+\?", targetInfo.select("a")[0].get("href"))[0][:-1]+"/about"))
    row += 1
workbook.close()

"""