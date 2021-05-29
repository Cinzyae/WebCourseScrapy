import scrapy
import scrapy.cmdline
import re
from fake_useragent import UserAgent
from myscrapy.webscrapy.items import WebscrapyItem


class TInfo(scrapy.Spider):
    name = "TInfo"
    allowed_domains = ["http://cs.hitsz.edu.cn/"]
    url_stop_words = []
    start_urls = [
        'http://cs.hitsz.edu.cn/szll/qzjs.htm'
        # 'http://cs.hitsz.edu.cn/szll/qzjs/%d.htm' % i for i in range(1, 6)
    ]

    def parse(self, response):
        item = WebscrapyItem()
        teacherlist = response.xpath('//div[@class="teacher-content"]/ul/li')
        for teacher in teacherlist:
            item['Title'] = teacher.xpath('div[@class="teacher-box"]/dl[1]/dd/text()').extract_first()
            yield item
        # TODO: add //a/@href into URL list


def runspider():
    scrapy.cmdline.execute(['scrapy', 'crawl', 'TInfo', '-o', 'TInfo.csv', '-t', 'csv'])


if __name__ == '__main__':
    runspider()
