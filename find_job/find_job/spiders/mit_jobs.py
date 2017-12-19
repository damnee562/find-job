import scrapy, re

from find_job.items import FindJobItem

class MitJobsSpider(scrapy.Spider):
    name = 'mit_jobs'

    def start_requests(self):
        url = 'https://mit.jobs/'
        keyword = getattr(self, 'keyword', None)
        if keyword is not None:
            url = 'https://mit.jobs/jobs?utf8=%E2%9C%93&search={}&c='.format(keyword)

        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for href in response.css('div.job-item div.main-title-item a::attr(href)'):
            yield response.follow(href, self.parse_details)

        next_page = response.css('div#job-list-result div.pagination a::attr(href)')
        if next_page is not None:
            next_page = 'https://mit.jobs' + next_page.extract_first()
            yield scrapy.Request(next_page, self.parse)

    def parse_details(self, response):
        month_dict = {
            'January': '01',
            'February': '02',
            'March': '03',
            'April': '04',
            'May': '05',
            'June': '06',
            'July': '07',
            'August': '08',
            'September': '09',
            'October': '10',
            'November': '11',
            'December': '12'
        }

        date_text = response.css('section.jobDetailInfo div.postedFrom span::attr(title)').extract_first().strip()
        date_list = re.split('[ |,]', date_text)

        item = FindJobItem()
        item['name'] = response.css('div.page-header-main h1 a::text').extract_first().strip()
        item['company'] = response.css('div.page-header-main h2 a::text').extract_first() or response.css('div.page-header-main h2::text').extract_first().strip()
        item['location'] = response.css('section.jobDetailInfo div.jobLocation').extract_first().split('</i> ')[1].split('\n')[0]
        item['salary'] = response.css('section.jobDetailInfo div.jobPayroll::text').extract_first().strip() + response.css('section.jobDetailInfo div.jobPayroll span::text').extract_first().strip()
        item['date'] = date_list[3] + '-' + month_dict[date_list[0]] + '-' + date_list[1]
        item['url'] = response.url

        yield item
