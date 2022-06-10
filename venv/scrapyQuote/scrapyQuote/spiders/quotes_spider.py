from urllib import response
import scrapy
from ..items import ScrapyquoteItem

class scrapyQuotes(scrapy.Spider):
#   define name and state Urls to scrap
    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
    #  create an instance of the items class 
        items = ScrapyquoteItem()

        all_div_quotes = response.css('div.quote')
        
        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            # assign response to the items 
            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            # send the response to pipeline to store in database
            # or u can save it in csv by running scrapy crawl -o items.csv 
            yield items
           
           
