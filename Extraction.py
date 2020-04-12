import requests
from bs4 import BeautifulSoup

url = 'https://news.google.com/covid19/map?hl=en-IN&gl=IN&ceid=IN:en'
url2 = 'https://worldometers.info/coronavirus/'

response = requests.get(url2)
#response.encoding  = 'UTF-8'

if response.status_code == 200:
    print('Connection Successfull ....')
    s = BeautifulSoup(response.text, 'html.parser', exclude_encodings=True)
    data = s.find_all('tr')
    # data2 = s.find_all('td')
    # index with 11 -> usa
    d = data[18].get_text(separator = '')
    my_list = list(d)
    val = ''
    for i in my_list:
        if i == '\n':
            val = val + ''
            continue
        else:
            val = val + i





else:
    print('Server Down, Try Agin later')
