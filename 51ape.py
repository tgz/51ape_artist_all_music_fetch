# -*- coding: utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup

page_encode = 'utf-8'

reload(sys)
sys.setdefaultencoding('utf-8')

def select_item_list(base_url, page_count, file_name):
    file = open('{}.txt'.format(file_name),'w')

    for index in range(1,page_count+1):
        url = '{}/index_{}.html'.format(base_url, index)
        if index == 1:
            url = '{}/index.html'.format(base_url)

        print('\n@@@@@@@\n start process page:{}'.format(url))

        r = requests.get(url)
        r.encoding = page_encode

        soup = BeautifulSoup(r.text)
        items = soup.select('div.news.w310.over.fl > ul > li')

        for item in items:
            index = item.select('span.number_no')[0].text
            name = item.select('a')[0].text
            url = item.select('a')[0]['href']

            download, passwd = get_netdisk_url_pass(url)
            print('index:{},name:{},url:{},\ndownload:{}, pass:{}'.format(index, name, url, download, passwd))
            print('\n')
            file.write('{} , {} , {} , {}\n'.format(index, name, download, passwd))
    file.close()


def get_netdisk_url_pass(url):
    r = requests.get(url)    
    r.encoding = page_encode
    soup = BeautifulSoup(r.text)
    download_url = soup.select('div.fl.over.w638 > a')[0]['href']
    passwd = soup.select('div.fl.over.w638 > b')[0].text
    return (download_url, passwd)


if __name__ == "__main__":
    base_url = 'http://www.51ape.com/jay'
    page_count = 8
    file_name = 'jay'

    select_item_list(base_url, page_count, file_name)


