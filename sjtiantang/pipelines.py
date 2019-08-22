# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
import scrapy

class SjtiantangPipeline(object):
    def process_item(self, item, spider):
        return item


class pptFilePipline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        # 获取文件下载路径
        item = request.meta['item']
        #  = urlparse(request.url).path
        # 根据文件名称保存
        # return join(basename(dirname(path)),basename(path))
        # return '%s' % (basename(item['file_name']))
        return '%s' % item['file_name']

    # 只能通过这个方法进行item传递
    def get_media_requests(self,item , info):
        # 只有文件下载的时候才需要
        if 'file_urls' in item.keys():
            for fileUrl in item['file_urls']:
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
                yield scrapy.Request(fileUrl,headers=headers,cookies=cookies, meta={'item': item})
        return item