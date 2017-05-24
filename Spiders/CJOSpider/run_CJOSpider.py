#!/usr/bin/env python3
# coding: utf-8
# File: runCJOAbbrFullSpider.py
# Author: lxw
# Date: 5/11/17 3:56 PM

# Supporting:
# 0. CAPTCHA(1st Generation)
# 1. User-Agent
# 2. IP Proxy(API: http://datazhiyuan.com:60001/plain)


from scrapy import cmdline
import sys

sys.path.append("/home/lxw/IT/projects/fintech_spider")
sys.path.append("/home/lxw/IT/projects/fintech_spider/Spiders/CJOSpider")


# cmdline.execute(["scrapy", "crawl", "CJO_Spider", "-L", "WARNING"])
cmdline.execute("scrapy crawl CJOSpider -L WARNING".split())


# redis-cli -h 192.168.1.29
# mongo 192.168.1.36:27017