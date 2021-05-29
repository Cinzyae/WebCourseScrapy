import scrapy
import scrapy.cmdline
from myscrapy.webscrapy.items import WebscrapyItem


class TInfo(scrapy.Spider):
    name = "TInfo"
    allowed_domains = ["hitsz.edu.cn"]
    url_stop_words = []
    start_urls = [
        'http://cs.hitsz.edu.cn/szll/qzjs.htm'
        # 'http://cs.hitsz.edu.cn/szll/qzjs/%d.htm' % i for i in range(1, 6)
    ]

    def parse(self, response):
        item = WebscrapyItem()
        teacherlist = response.xpath('//div[@class="teacher-content"]/ul/li')
        for teacher in teacherlist:
            item['Name'] = teacher.xpath('div[@class="teacher-left"]/p[@class="teacher-name"]/text()').extract_first()
            item['Title'] = teacher.xpath('div[@class="teacher-box"]/dl[1]/dd/text()').extract_first()
            item['Phone'] = teacher.xpath('div[@class="teacher-box"]/dl[2]/dd/text()').extract_first()
            item['Fax'] = teacher.xpath('div[@class="teacher-box"]/dl[3]/dd/text()').extract_first()
            item['Email'] = teacher.xpath('div[@class="teacher-box"]/dl[4]/dd/a/text()').extract_first()
            item['ResearchDirection'] = teacher.xpath('div[@class="teacher-box"]/dl[5]/dd/text()').extract_first()
            yield item

        url_list = response.xpath("//a/@href").extract()
        for url in url_list:
            if url[0:4] != 'qzjs':
                continue
            url = 'http://cs.hitsz.edu.cn/szll/' + url
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)


def runspider():
    scrapy.cmdline.execute(['scrapy', 'crawl', 'TInfo', '-o', 'TInfo.csv', '-t', 'csv'])


if __name__ == '__main__':
    runspider()
