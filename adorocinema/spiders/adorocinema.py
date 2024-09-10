from scrapy import Spider, Request

# exemplo de XPath: //a[@class='meta-title-link'] - Encontra todos os elementos em que a classe seja igual a meta-title-link
# exemplo de XPath: //a[contains(@class,'meta-title-link')] - Encontra todos os elementos em que a classe contenha meta-title-link

class AdoroCinemaSpider(Spider):
    name = 'adorocinema'
    start_urls = ['https://www.adorocinema.com/filmes/melhores/',]
    page = 1

    def parse(self, response):
        movies = response.xpath("//div[contains(@class,'card-list')]")
        for movie in movies:
            yield {
                "title": movie.css("a.meta-title-link::text").get(),
                "duration": movie.css("div.meta-body-info::text").get().replace("\n", ""),
                "original_title": movie.xpath("div[1]//div[@class='meta-body-item']/span[@class='dark-grey']/text()").get(),
            }
        self.page += 1
        yield Request(f'https://www.adorocinema.com/filmes/melhores/?page={self.page}', self.parse)