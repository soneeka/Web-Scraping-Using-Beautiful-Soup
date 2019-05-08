import bs4 as bs
import urllib.request

for id in range (1,2385):
    try:
        print (id)
        fetchurl = "http://apps.who.int/gho/indicators/?id="+ str(id)
        source = urllib.request.urlopen(fetchurl).read()
        soup = bs.BeautifulSoup(source,'xml')

        for i in soup.find('Name'):
            print(i)

        for j in soup.find('Definition'):
            print(j)
        print('\n')
        print('\n')
    
    except:
        pass