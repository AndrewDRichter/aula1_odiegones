from scrapy import Spider

class AdoroCinemaSpider(Spider):
    name = 'adorocinema'
    start_urls = 'https://www.adorocinema.com/filmes/melhores'