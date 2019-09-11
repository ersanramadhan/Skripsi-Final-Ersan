import os
from bs4 import BeautifulSoup as bs


os.chdir("D:\skripsi\crawling")
fData = 'testing2.html'
fName = 'search_twittertesting4.csv'


if __name__ =="__main__":
    print('Loading Data: ', flush=True)
    soup = bs(open(fData, encoding='utf-8', errors='ignore', mode='r'), 'html.parser')
    data = soup.find_all('li', class_='js-stream-item stream-item stream-item\n')

    print('Importing Tweets: ', flush=True)
    Tweets = [t.find_all('p', class_='TweetTextSize js-tweet-text tweet-text')[0] for t in data]
    Tweets = [bs(str(t), 'html.parser').text for t in Tweets]
    Tweets = [t.replace(',', ' ') for t in Tweets]

    print('Loading Time: ', flush = True)
    waktu = [t.find_all('a',class_='tweet-timestamp js-permalink js-nav js-tooltip')[0] for t in data]
    waktu = [bs(str(t),'html.parser').text for t in waktu]

# dfile = open(fName, 'w')
# dfile.write('Tweet\n')
# for tw in Tweets:
#     dfile.write('%s\n'% (str(tw.encode('ascii', 'replace'))[2:-1]))
# dfile.close()


    dfile = open(fName,'w')
    dfile.write('Time,Tweet\n')
    for t,tw in zip(waktu,Tweets):
        dfile.write('%s,%s\n' %(t,(str(tw.encode('ascii','replace'))[2:-1])))
    dfile.close()

print('All Finished', flush=True)