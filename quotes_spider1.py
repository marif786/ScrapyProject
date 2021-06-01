import scrapy


class QuotesSpider(scrapy.Spider):
    name = "web"
    working = "Working correctly"
    print(working)

    start_urls = [
        'https://www.dallascad.org/AcctDetailRes.aspx?ID=380875100F0070000',
    ]

    def parse(self, response):
        yield {
            'Col EW': response.xpath('//span[@id="lblOwner"]/following-sibling::text()').extract()[0],
            'Col EZ': response.xpath('//span[@id="lblOwner"]/following-sibling::text()').extract()[1],
            'Col EW': response.xpath('//span[@id="lblOwner"]/following-sibling::text()').extract()[2],
            'Col FD': response.xpath('//span[@id="lblOwner"]/following-sibling::text()').extract()[2],
            'Col FE': response.xpath('//span[@id="lblOwner"]/following-sibling::text()').extract()[2],
            'Col FE': response.xpath('//span[@id="lblOwner"]/following-sibling::text()').extract()[2],
            'Col FH': response.xpath('//span[@id="lblOwner"]/following-sibling::text()').extract()[2],


            'Col AZ': response.xpath('//table[@id="MultiOwner1_dgmultiOwner"]/tr[2]/td[2]/text()').extract_first(),
        }



