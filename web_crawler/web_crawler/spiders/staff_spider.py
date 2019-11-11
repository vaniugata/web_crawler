import scrapy

class StaffSpider(scrapy.Spider):
    name = "staff"
    url = 'https://www.fmi.uni-sofia.bg/bg/faculty-staff'

    def start_requests(self):
            yield scrapy.Request(url = self.url, callback = self.crawl_page) 

    def crawl_page(self, response):
        print('next_page')
        for entry in response.xpath('//h3'):
            url = 'https://www.fmi.uni-sofia.bg' + str(entry.xpath('a/@href').get())
            yield scrapy.Request(url = url, callback=self.parse)
    
    def parse(self, response):
        print( response.xpath('//h1/text()').get() )
        yield {
            'name': response.xpath('//h1/').get().encode('utf-8')
        }
        #write data to file
        # with open('content.txt', 'w') as f:
            # f.write(response.selector.xpath('//div/text()').get())
