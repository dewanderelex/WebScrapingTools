import bs4, requests, os, xlsxwriter, time, multiprocessing

start_time = time.time()



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

workbook = xlsxwriter.Workbook('PhoDiemData1.xlsx')
worksheet = workbook.add_worksheet()
row = 2
col = 0

def abc(n):
    link = 'https://news.zing.vn/tra-cuu-diem-thi-thpt-2017-ket-qua.html?text=' + generateID(n)
    res = requests.get(link)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    participantInfo = soup.select('.table td')
    return participantInfo


if __name__ =='__main__':

    for count in range (25004950,25005000,1):
        p = multiprocessing.Process(target=abc(count))
        if abc != []:
            worksheet.write(row, col, abc(count)[0].text)
            worksheet.write(row, col + 1, abc(count)[1].text)
            worksheet.write(row, col + 2, abc(count)[2].text)
            worksheet.write(row, col + 3, abc(count)[3].text)
            worksheet.write(row, col + 4, abc(count)[5].text)
            row += 1
        p.start()
    workbook.close()
print("--- %s seconds ---" % (time.time() - start_time))