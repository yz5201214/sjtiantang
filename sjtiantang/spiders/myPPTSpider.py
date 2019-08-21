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
        'UM_distinctid': '16cb32a59591-0f34aedf1c94fb-c343162-1fa400-16cb32a595a50c',
        'CNZZDATA1277386113': '828220532-1566369342-%7C1566374777',
        'JSESSIONID': 'D68BB15C560D34A050F58A5F0A373EC2',
        'ksqw': 'fe288eb4aca6447bb59d66c12a4b4d1b',
        'lkj_au': '458c098f2f4b43b2a357e4c0116623aa',
        'nnj_ooi': 'a18d7c3579128123dd6d3765e13088deec2b653a34c488374b7488796f374887',
        'olp_ctt': 'e5d356896c390ee6'
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,headers=self.headers,cookies=self.cookies,callback=self.parse)

    def parse(self, response):
        '''
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
                # yield scrapy.Request(url=next_url,headers=self.headers,callback=self.parse)
        '''
