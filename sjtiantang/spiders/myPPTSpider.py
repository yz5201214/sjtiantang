import scrapy


from sjtiantang.items import testFileItem

class pptSpider(scrapy.Spider):
    name = 'pptSpider'
    start_urls = [
        'https://www.sjtiantang.com/category/ppt'
    ]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }
    cookies = {
        'UM_distinctid': '16c199bd3c76e9-02cdd9ad00735a-c343162-384000-16c199bd3c836',
        'CNZZDATA1277386113': '1693883798-1563797052-%7C1566398760',
        'JSESSIONID': '557A746E3BA03E913268B3F61B6F2C2B',
        'ksqw': '0045a5659f07428e8eceb57e8dff1775',
        'lkj_au': '94de4d4f3d7d4907b8a833763d061840',
        'nnj_ooi': 'ad4535995666123c1b64967876b41f76556d78e7a22907ff4b7488796f374887',
        'olp_ctt': 'e5d356896c390ee6'
    }
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,headers=self.headers,cookies=self.cookies,callback=self.parse)

    def parse(self, response):
        divRowAList = response.css('div.row a')
        for divItem in divRowAList:
            downUrl = divItem.css('a::attr("href")').extract_first()
            realUrl = "https://www.sjtiantang.com/download/"+downUrl[1:len(downUrl)].split('/')[1]
            realName = divItem.css('div.show-piece-info span::text').extract_first().replace(' ','-')
            pptFileItem = testFileItem()
            pptFileItem['file_urls'] = [realUrl]
            pptFileItem['file_name'] = realName+".pptx"
            yield pptFileItem

        pageDivList = response.css('#cut-page a')
        for pageA in pageDivList:
            if pageA.css('i::attr("class")').extract_first() == 'fa fa-angle-right':
                next_url = "https://www.sjtiantang.com/category/ppt?sort=default&page="+pageA.css('a::attr("data-num")').extract_first()
                yield scrapy.Request(url=next_url,headers=self.headers,cookies=self.cookies,callback=self.parse)