import scrapy

from find_job.items import FindJobItem

class InsideJobsSpider(scrapy.Spider):
    name = 'inside_jobs'

    def start_requests(self):
        url = 'https://jobs.inside.com.tw'
        keyword = getattr(self, 'keyword', None)
        if keyword is not None:
            url = 'https://jobs.inside.com.tw/jobs/index?k={}'.format(keyword)

        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for href in response.css('div.list-group a.list-group-item::attr(href)'):
            yield response.follow(href, self.parse_details)

        next_page = response.css('ul.pagination li')[-1].css('a::attr(href)').extract_first()

        if next_page is not None and next_page != '/jobs/index?k={}'.format(self.keyword):
            yield response.follow(next_page, self.parse)

    def parse_details(self, response):
        item = FindJobItem()
        item['company'] = response.css('div.col-sm-9 div.panel-heading h1::text').extract_first().strip()
        item['name'] = response.css('div.col-sm-8 h1::text').extract_first().strip()
        item['location'] = response.css('div.col-sm-8 p::text')[1].extract().split('：')[1].strip()
        item['salary'] = response.css('div.col-sm-8 p::text')[2].extract().split('：')[1].strip()
        item['date'] = response.css('div.col-sm-8 p::text')[3].extract().split('：')[1].strip()
        item['url'] = response.url

        yield item
