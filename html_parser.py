# -*- coding=utf-8 -*-
from pyquery import PyQuery as pq
import outputer


class Parser(object):
    def __init__(self, root_url):
        self.root_url = root_url
        self.outputer = outputer.Outputer()

    def parse(self, html_cont, url):
        doc = pq(html_cont)
        new_urls = self._get_new_urls(doc)
        self._get_new_datas(doc, url)
        return new_urls

    def _get_new_urls(self, doc):
        new_urls = list()
        items = doc('#industrynav li').items()
        for item in items:
            new_url = item.find('a').attr('href')
            new_full_url = ''.join([self.root_url, new_url])
            new_urls.append(new_full_url)

        return new_urls

    def _get_new_datas(self, doc, url):
        items = doc('#industrynav li').items()
        sign = url.split('/')[-1]
        title = ''
        for item in items:
            if item.find('a').attr('href') == sign:
                title = item.find('a').text()
        if title == '':
            return
        html1 = doc('#datatbl')
        doc = pq(html1)
        items2 = doc('tbody tr').items()
        for item in items2:
            dict_1 = {
                '板块': item.find('td:nth-child(1)').text(),
                '公司家数': item.find('td:nth-child(2)').text(),
                '平均价格': item.find('td:nth-child(3)').text(),
                '涨跌额': item.find('td:nth-child(4)').text(),
                '涨跌幅': item.find('td:nth-child(5)').text(),
                '总成交量(手)': item.find('td:nth-child(6)').text(),
                '总成交额(万元)': item.find('td:nth-child(7)').text(),
                '领涨股': item.find('td:nth-child(8) > a').text(),
                '领涨股代码': item.find('td:nth-child(8)').text().split()[-1][1:-1],
                '领涨股涨跌幅': item.find('td:nth-child(9)').text(),
                '当前价': item.find('td:nth-child(10)').text(),
                '领涨股涨跌额': item.find('td:nth-child(11)').text(),
            }
            print('---------------------------------------------')
            list_data = []
            for key in dict_1:
                list_data.append(dict_1[key])

            list_data.append(item.find('a').attr('href'))
            list_data.append(item.find('.border > a').attr('href'))
            list_data.append(title)

            # print('sign:', sign)
            print('page url:', url)
            # print(item.find('a').attr('href'))
            # print(item.find('.border > a').attr('href'))
            # print(list_data)
            self.outputer.collect_data(list_data)

