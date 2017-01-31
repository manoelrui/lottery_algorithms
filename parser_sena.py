from bs4 import BeautifulSoup

soup = BeautifulSoup(open('D_MEGA.HTM','r'), 'html.parser')
file = open('sena_parsed.csv','w')

for tr in soup.find_all('tr'):
    find_all = tr.find_all('td')
    if len(find_all)>2:
        join = ",".join(["'"+td.get_text().encode('ascii', 'ignore')+"'" for td in find_all])
        file.write(join+'\n')
