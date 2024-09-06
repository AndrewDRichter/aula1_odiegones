from scrapy import Spider

# exemplo de XPath: //a[@class='meta-title-link'] - Encontra todos os elementos em que a classe seja igual a meta-title-link
# exemplo de XPath: //a[contains(@class,'meta-title-link')] - Encontra todos os elementos em que a classe contenha meta-title-link

class AdoroCinemaSpider(Spider):
    name = 'adorocinema'
    start_urls = 'https://www.adorocinema.com/filmes/melhores'

    def parse(self, response):
        pass