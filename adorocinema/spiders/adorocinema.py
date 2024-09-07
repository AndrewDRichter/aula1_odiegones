from scrapy import Spider

# exemplo de XPath: //a[@class='meta-title-link'] - Encontra todos os elementos em que a classe seja igual a meta-title-link
# exemplo de XPath: //a[contains(@class,'meta-title-link')] - Encontra todos os elementos em que a classe contenha meta-title-link

class AdoroCinemaSpider(Spider):
    name = 'adorocinema'
    start_urls = ['https://www.adorocinema.com/filmes/melhores/',]

    def parse(self, response):
        movies = response.xpath("//div[contains(@class,'card-list')]")
        for movie in movies:
            yield {
                "title": movie.css("a.meta-title-link::text").get(),
                "duration": movie.css("div.meta-body-info::text").get().replace("\n", ""),
                "original_title": movie.xpath("div[1]//div[@class='meta-body-item']/span[@class='dark-grey']/text()").get(),
            }