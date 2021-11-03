import scrapy
from ygdy.models import Movie

class YgdyspiSpider(scrapy.Spider):
    name = 'ygdyspi'
    allowed_domains = ['www.dydytt.net']
    start_urls = ['http://www.dydytt.net/']

    def start_requests(self):
        base_url = 'https://www.dydytt.net/html/gndy/{}/index.html'
        categories = ['china', 'rihan', 'oumei', 'dyzz']
        for category in categories:
            yield scrapy.Request(base_url.format(category),callback=self.parse)

    def parse(self, response):
        detail_urls = response.xpath('//a[@class="ulink"]/@href').extract()
        detail_urls = [url for url in detail_urls if 'index' not in url]
        # print(detail_urls)

        for url in detail_urls:
            yield scrapy.Request(response.urljoin(url), callback=self.detail)
        next_page = response.xpath('.//a[contains(text(),"下一页")]/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def detail(self,response):
        title = response.xpath('//div[@class="title_all"]/h1/font/text()').extract_first() #这里是他的title，没有在zoom里面
        zoom = response.xpath('//div[@id="Zoom"]')[0]
        img = zoom.xpath('.//img//@src').extract_first()
        tran_name = zoom.xpath('.//text()').re('◎译\u3000\u3000名\u3000(.*)')
        name = zoom.xpath(' .//text()').re('◎片\u3000\u3000名\u3000(.*)')
        year = zoom.xpath('.//text()').re('◎年\u3000\u3000代\u3000(.*)')
        country = zoom.xpath('.//text()').re('◎产\u3000\u3000地\u3000(.*)')
        category = zoom.xpath('.//text()').re('◎类\u3000\u3000别\u3000(.*)')
        douban_rate = zoom.xpath('.//text()').re('◎豆瓣评分\u3000(.*)')
        language = zoom.xpath('.//text()').re('◎语\u3000\u3000言\u3000(.*)')
        publish_date = zoom.xpath('.//text()').re('◎上映日期\u3000(.*)')
        movie_time = zoom.xpath('.//text()').re('◎片\u3000\u3000长\u3000(.*)')
        director = zoom.xpath('.//text()').re('◎导\u3000\u3000演\u3000(.*)')
        main_actor = zoom.xpath('.//text()').re('◎主\u3000\u3000演\u3000(.*)')
        download_url =zoom.xpath('.//a/@href').extract_first()
        Movie.objects.create(title = title,img=img,tran_name=tran_name,name=name,year= year,country=country,
                             category=category,douban_rate=douban_rate,language=language,publish_date=publish_date,
                             movie_time = movie_time,director=director,main_actor=main_actor,download_url=download_url,
                             )
