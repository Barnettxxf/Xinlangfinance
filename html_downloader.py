# -*- coding=utf-8 -*-
import time
from selenium import webdriver
import requests


class HtmlDownloader(object):
        def __init__(self):
                self.meta = False
                self.driver = None

        def downloader(self):
                self.meta = True
                self.driver = webdriver.PhantomJS()

        def download(self, url):
                print('=======================================')
                print('download url:', url)
                print('meta:', self.meta)
                self.driver = webdriver.PhantomJS()
                if 1:
                        self.driver.get(url)
                        time.sleep(5)
                        html = self.driver.page_source
                        print('driver url', self.driver.current_url)
                else:
                        html = requests.get(url).text
                self.driver.close()
                return html

        def close(self):
                self.driver.close()
