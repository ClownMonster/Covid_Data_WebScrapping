import requests
from bs4 import BeautifulSoup

from DataFormat import dataformat # to format the data
import WriteToExcel

#url1 = 'https://news.google.com/covid19/map?hl=en-IN&gl=IN&ceid=IN:en'
url2 = 'https://worldometers.info/coronavirus/'

response = requests.get(url2)
#response.encoding  = 'UTF-8'

if response.status_code == 200:
    print('Connection Successfull ....')
    s = BeautifulSoup(response.text, 'html.parser')
    data = s.find_all('tr')
    try:
        for i in range(9, 443):
            d = data[i].get_text(separator = '')
            formated_data = dataformat(d)
            print(formated_data)
            WriteToExcel.write_the_data(formated_data)
    except:
        print('Completed..')
        WriteToExcel.save_close()

    '''
    formated_data[1]  Country Name
    formated_data[2]  Total Cases
    formated_data[3]  New Cases
    formated_data[4]  Total Deaths
    formated_data[5]  New Deaths
    formated_data[6]  Total Recovered
    formated_data[7]  Total Active Cases
    formated_data[8]  Critical Cases
    formated_data[9]  Total Cases per 1M
    formated_data[10]  Total Deaths per 1M
    formated_data[11] Total Tests Done

    '''
else:
    print('Server Down, Try Agin later')
