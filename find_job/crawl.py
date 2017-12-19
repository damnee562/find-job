import argparse

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--keyword', required=True)
args = parser.parse_args()
keyword = args.keyword

setting = get_project_settings()
process = CrawlerProcess(setting)

for spider_name in process.spiders.list():
    print ("Running spider {}".format(spider_name))
    process.crawl(spider_name, keyword=keyword)

process.start()
