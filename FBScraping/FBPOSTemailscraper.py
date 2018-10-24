import os, bs4, requests, xlsxwriter, re, sys, codecs

workbook = xlsxwriter.Workbook("Product/DataFBPost.xlsx")
worksheet = workbook.add_worksheet()
row = 2
col = 0

#Open Data and place the data into BeautifulSoup model
data = open("Raw Data/DataFBPost.txt", "r").read()  #<------------------------------------
soup = bs4.BeautifulSoup(data, "html.parser")
emailData = soup.find_all("div", attrs = {"class" : "UFIReplyList"})[2]

for email in emailData:
    col = 0
    email_2 = email.find_all(attrs = {"class": "UFICommentBody"})
    if email_2 != []:
        email_3 = email_2[0].find_all("span")
        if email_3 != []:
            print (email_3)
            for emailHTML in email_3:
                regexEmail = re.findall("\S+@gmail\.com", emailHTML.text)
                if regexEmail != []:
                    worksheet.write(row, col, regexEmail[0])
                    row += 1





#Close the Workbook to create file.
workbook.close()
