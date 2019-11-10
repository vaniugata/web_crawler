import scrapy

class StaffSpider(scrapy.Spider):
    name = "staff"

    def start_requests(self):
        urls = ['https://www.fmi.uni-sofia.bg/bg/faculty-staff']

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse) 
    
    def parse(self, response):
        yield {
            'name': response.xpath('//a/text()').getall()
        }
        #write data to file
        # with open('content.txt', 'w') as f:
            # f.write(response.selector.xpath('//div/text()').get())
