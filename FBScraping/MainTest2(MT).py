import multiprocessing,time, bs4, requests, os, xlsxwriter
from multiprocessing import Pool
start_time = time.time()

workbook = xlsxwriter.Workbook('PhoDiemData3.xlsx')
worksheet = workbook.add_worksheet()
class sV:
    row = 2
    col = 0

def generateID(n):
    canID = str(n)
    count = 0
    num = n
    while num > 0:
        count += 1
        num//=10
    count0 = 8 - count
    for i in range (count0):
        canID = "0" + canID
    return canID

def getInfoList(n):
    link = 'https://news.zing.vn/tra-cuu-diem-thi-thpt-2017-ket-qua.html?text=' + generateID(n)
    res = requests.get(link)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    participantInfo = soup.select('.table td')
    """
    if participantInfo != []:
        print (participantInfo[1])
#Test
    """
    """
    returnVal = []
    for i in [0, 1, 2, 3, 5]:
        returnVal.append(participantInfo[i].text)
    return returnVal
    """
    if participantInfo != []:
        worksheet.write(sV.row, sV.col, participantInfo[0].text)
        worksheet.write(sV.row, sV.col + 1, participantInfo[1].text)
        worksheet.write(sV.row, sV.col + 2, participantInfo[2].text)
        worksheet.write(sV.row, sV.col + 3, participantInfo[3].text)
        worksheet.write(sV.row, sV.col + 4, participantInfo[5].text)
        sV.row += 1


if __name__ == '__main__':
        pool = Pool(processes=15)
        pool.map(getInfoList,range (25004950, 25005000,1))
workbook.close()

print("--- %s seconds ---" % (time.time() - start_time))