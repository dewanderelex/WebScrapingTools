import bs4, requests, os, xlsxwriter, time

start_time = time.time()

def generateID(n):
    canID = str(n)
    count = 0
    num = n
    while num > 0:
        count += 1
        num//=10
    count0 = 4 - count
    for i in range (count0):
        canID = "0" + canID
    return canID
'''
workbook = xlsxwriter.Workbook('PhoDiemData.xlsx')
worksheet = workbook.add_worksheet()
row = 2
col = 0


for count in range (1000000):
    link = 'https://news.zing.vn/tra-cuu-diem-thi-thpt-2017-ket-qua.html?text=' + "01" + generateID(count)
    res = requests.get(link)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    participantInfo = soup.select('.table td')
    if participantInfo != []:
        worksheet.write(row, col, participantInfo[0].text)
        worksheet.write(row, col + 1, participantInfo[1].text)
        worksheet.write(row, col + 2, participantInfo[2].text)
        worksheet.write(row, col + 3, participantInfo[3].text)
        worksheet.write(row, col + 4, participantInfo[5].text)
        row += 1

workbook.close()
'''

count = 747
link = 'https://news.zing.vn/tra-cuu-diem-thi-thpt-2017-ket-qua.html?text=' + "0101" + generateID(count)

print("--- %s seconds ---" % (time.time() - start_time))
