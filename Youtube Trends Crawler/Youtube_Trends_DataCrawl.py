import csv
from bs4 import BeautifulSoup

source = open('Trending - YouTube.html', encoding='utf-8')



soup = BeautifulSoup(source, 'lxml')

with open('trendingLinks.csv', 'w',newline='', encoding='utf-8') as csvwritefile:

   
    
    
    csvwriter = csv.writer(csvwritefile)
    
    csvwriter.writerow(['titles', 'links'])

    for renderer in soup.find_all('a', 'yt-simple-endpoint style-scope ytd-video-renderer'):
        titles= renderer['title']
        try:
            links = renderer['href']
        except Exception as e:
                href = None
                print(e.__str__)
    
        csvwriter.writerow([titles,links])
csvwritefile.close()

