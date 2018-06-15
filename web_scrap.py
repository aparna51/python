import urllib.request
from bs4 import BeautifulSoup
website="https://php.net"

webdata=urllib.request.urlopen(website)
clean_data=webdata.read()

get_clean=BeautifulSoup(clean_data,'html5lib')
final_data=get_clean.get_text()
print(final_data)
