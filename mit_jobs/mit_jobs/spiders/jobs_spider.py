import scrapy

from mit_jobs.items import MitJobsItem

class JobsSpider(scrapy.Spider):
    name = 'jobs'

    def start_requests(self):
        url = 'https://mit.jobs/'
        keyword = getattr(self, 'keyword', None)
        if keyword is not None:
            url = 'https://mit.jobs/jobs?utf8=%E2%9C%93&search={}&c='.format(keyword)

        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        with open('./url.txt', 'w') as f:
            f.write(response.url + '\n')

        for href in response.css('div.job-item div.main-title-item a::attr(href)'):
            yield response.follow(href, self.parse_details)

        next_page = response.css('div#job-list-result div.pagination a::attr(href)')
        if next_page is not None:
            next_page = 'https://mit.jobs' + next_page.extract_first()
            yield scrapy.Request(next_page, self.parse)

    def parse_details(self, response):
        item = MitJobsItem()
        item['name'] = response.css('div.page-header-main h1 a::text').extract_first().strip(),
        item['company'] = response.css('div.page-header-main h2 a::text').extract_first() or response.css('div.page-header-main h2::text').extract_first().strip(),
        item['salary'] = response.css('section.jobDetailInfo div.jobPayroll::text').extract_first().strip() + response.css('section.jobDetailInfo div.jobPayroll span::text').extract_first().strip(),
        item['location'] = response.css('section.jobDetailInfo div.jobLocation').extract_first().split('</i> ')[1].split('\n')[0],
        item['url'] = response.url

        yield item
