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
        print('---------%s' % request.headers)
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
                    'UM_distinctid': '16cb32a59591-0f34aedf1c94fb-c343162-1fa400-16cb32a595a50c',
                    'CNZZDATA1277386113': '828220532-1566369342-%7C1566374777',
                    'JSESSIONID': 'D68BB15C560D34A050F58A5F0A373EC2',
                    'ksqw': 'fe288eb4aca6447bb59d66c12a4b4d1b',
                    'lkj_au': '458c098f2f4b43b2a357e4c0116623aa',
                    'nnj_ooi': 'a18d7c3579128123dd6d3765e13088deec2b653a34c488374b7488796f374887',
                    'olp_ctt': 'e5d356896c390ee6'
                }
                yield scrapy.Request(fileUrl, meta={'item': item})
        return item