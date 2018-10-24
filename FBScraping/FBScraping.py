import os, bs4, requests, xlsxwriter, re, sys, codecs

"""
6 TXT File to include:
    DataHoiDuHocSinhMy
    DataHoiSAT
    DataIELTSNgocBach
    DataIELTSShare
    DataIELTSViet
    DataSATHitTarget
"""


#Creating Workbook and Worksheet
workbook = xlsxwriter.Workbook("Product/DataIELTSViet.xlsx")      #<---------------------------------
worksheet = workbook.add_worksheet()

#Initialize row and column to write in worksheet
row = 1
column = 0

"""
#Initilizing Codecs
sys.stdout = codecs.getwriter('utf_8')(sys.__stdout__)
sys.stdin = codecs.getreader('utf_8')(sys.__stdin__)
"""

#Open Data and place the data into BeautifulSoup model
data = open("Raw Data/DataIELTSViet.txt", "r")             #<------------------------------------
soup = bs4.BeautifulSoup(data.read(), "html.parser")
infoList = soup.find_all("div", attrs = {"class" : "_6a _6b"})

a = 0

#Working with data and write into worksheet
for info in infoList:
    if info == []:
        break
    column = 0
    soupLink = info.find_all("div", attrs= {"class": "_60ri fsl fwb fcb"})
    if soupLink != []:
        name = soupLink[0].find("a").text
        if re.findall("php\?id=\d+", str(soupLink[0])) != []:
            soupLink = "https://www.facebook.com/" + re.findall("php\?id=\d+", str(soupLink[0]))[0][7:]
        else: soupLink = re.findall("https:\S+\?", str(soupLink[0]))[0][:-1]
        worksheet.write(row, column, name)
        worksheet.write(row, column + 1, soupLink)
    soupInfo = info.find_all("div", attrs={"class" : "_60rj"})
    timeInfo = re.findall('title=".+"\>\<s', str(info))
    if soupInfo != []:
        if timeInfo != []:
            for information in soupInfo:
                worksheet.write(row, column + 2, timeInfo[0][7:-4])
                worksheet.write(row, column + 3, information.text)
        else:
            for information in soupInfo:
                worksheet.write(row, column + 2, information.text)
        column += 1
    #Chong Cach Dong
    a += 1
    if a % 4 == 0:
        a = 0
        row += 1

#Close the Workbook to create file.
workbook.close()
