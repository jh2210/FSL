import datetime as datetime
from urllib.request import urlopen
import bs4 as bs
CN = str(input('Enter your candidate number: '))
dates = []
rooms = []
start = []
finish = []
exam = []
url = 'https://www.friendsict.org/Exams/mytimetable2.php?ExamNumber='+CN+'&Submit=submit'
html = urlopen(url).read()
soup = bs.BeautifulSoup(html,'lxml')
table = soup.find('table')
rows = table.find_all('tr')
for row in rows:
    dates.append(str(row.find_all('td')[0].text))
    rooms.append(str(row.find_all('td')[1].text))
    start.append(str(row.find_all('td')[2].text))
    finish.append(str(row.find_all('td')[3].text))
    exam.append(str(row.find_all('td')[4].text))

del dates[0]
del rooms[0]
del start[0]
del finish[0]
del exam[0]

Events = []
Fixed = []
Date = []
Fixed2=[]

n = len(dates)
i=0
today = str(datetime.date.today());
curr_year = int(today[:4]);


while (i<n):
    i=i+1
for i in range(n):
    x = dates[i].split(" ")
    del x[0]
    x= x[0]+' '+x[1]+' '+str([curr_year][0])
    Fixed.append(str(x))
    z = Fixed[i].split(" ")
    z_int= int(z[0])
    if z_int<10:
         N=1
         g= z[0].rjust(N + len(z[0]), '0') 
         g= g+' '+z[1]+' '+z[2]
    if z_int>10:
        g=z[0]+' '+z[1]+' '+z[2]
    Fixed2.append(str(g))

    x= exam[i]+' '+rooms[i]
    Events.append(str(x))

FinalDates=[]
while (i<n):
    i=i+1
for i in range(n):
   d = datetime.datetime.strptime(Fixed2[i], '%d %B %Y').date()
   d.strftime('%Y-%m-%d')
   FinalDates.append(str(d))

import pandas as pd 

df = pd.DataFrame(list(zip(FinalDates, start, finish, Events)), 
               columns =['Start Date', 'Start Time', 'End Time', 'Subject']) 
df.to_csv('Timetables'+CN+'.csv') 

    
    

    