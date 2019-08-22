import scrapy


from sjtiantang.items import testFileItem

class pptSpider(scrapy.Spider):
    name = 'pptSpider'
    start_urls = [
        'https://www.sjtiantang.com/category/ppt',# ppt
        'https://www.sjtiantang.com/category/resume',# 简历
        'https://www.sjtiantang.com/category/font',  # 字体
    ]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }
    cookies = {
        'UM_distinctid': '16cb32a59591-0f34aedf1c94fb-c343162-1fa400-16cb32a595a50c',
        'CNZZDATA1277386113': '828220532-1566369342-%7C1566442304',
        'JSESSIONID': '311197EE6556F7A9C8CF0DDB0C448A11',
        'ksqw': '0045a5659f07428e8eceb57e8dff1775',
        'lkj_au': '458c098f2f4b43b2a357e4c0116623aa',
        'nnj_ooi': 'a18d7c3579128123dd6d3765e13088deec2b653a34c488374b7488796f374887',
        'olp_ctt': 'e5d356896c390ee6'
    }
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,headers=self.headers,cookies=self.cookies,callback=self.parse)

    def parse(self, response):
        if response.url.find('resume') > -1:
            folder = 'resume/'
            suffix = '.docx'
        if response.url.find('ppt') > -1:
            folder = 'ppt/'
            suffix = '.pptx'
        if response.url.find('font') > -1:
            folder = 'font/'
            suffix = '.ttf'
        divRowAList = response.css('div.row a')
        x = 0
        for divItem in divRowAList:
            downUrl = divItem.css('a::attr("href")').extract_first()
            realUrl = "https://www.sjtiantang.com/download/"+downUrl[1:len(downUrl)].split('/')[1]
            realName = divItem.css('div.show-piece-info span::text').extract_first().replace(' ','-')+'--'+str(x)
            pptFileItem = testFileItem()
            pptFileItem['file_urls'] = [realUrl]
            pptFileItem['file_name'] = folder + realName+suffix
            yield pptFileItem
            x = x +1

        pageDivList = response.css('#cut-page a')
        for pageA in pageDivList:
            if pageA.css('i::attr("class")').extract_first() == 'fa fa-angle-right':
                next_url = "https://www.sjtiantang.com/category/ppt?sort=default&page="+pageA.css('a::attr("data-num")').extract_first()
                # yield scrapy.Request(url=next_url,headers=self.headers,cookies=self.cookies,callback=self.parse)