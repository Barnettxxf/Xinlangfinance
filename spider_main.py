# -*- coding=utf-8 -*-


import url_manager
import html_downloader
import html_parser
import outputer


class SpiderMain(object):
        def __init__(self, url):
                self.urls = url_manager.UrlManager()
                self.downloader = html_downloader.HtmlDownloader()
                self.parser = html_parser.Parser(url)
                self.outputer = outputer.Outputer()
                self.root_url = url

        def crawl(self):
                self.outputer.creat_outputer()
                self.urls.add_new_url(self.root_url)

                while self.urls.has_new_url():
                        new_url = self.urls.get_new_url()
                        print('new_url', new_url)
                        html_cont = self.downloader.download(new_url)
                        new_urls = self.parser.parse(html_cont, new_url)
                        self.urls.add_new_urls(new_urls)
                self.outputer.outputer()
                print('crawl finished')


if __name__ == '__main__':
        root_url = 'http://finance.sina.com.cn/stock/sl/'
        spider = SpiderMain(root_url)
        spider.crawl()
