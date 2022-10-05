# import urlparse
import scrapy

from scrapy.http import Request

class MIDL21Spider(scrapy.Spider):
    name = "MIDL21_Proceedings"

    def start_requests(self):
        urls = [
            'https://proceedings.mlr.press/v143/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = f'{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')

        # response.xpath('/html/body/main/div/div[*]/p[3]/a[2]/@href').getall()


        for article in response.xpath('/html/body/main/div/div[*]'):
            # yield {
            #     'title': article.xpath('p[1]/text()').get(),
            #     'filelink': article.xpath('p[3]/a[2]/@href').get(),
            # }
            try:
                yield Request(
                    url=article.xpath('p[3]/a[2]/@href').get(),
                    meta={
                        "title": article.xpath('p[1]/text()').get()
                        },
                    callback=self.save_pdf
                )
            except Exception as e:
                print(e)

    def save_pdf(self, response):
        try:
            # path = response.url.split('/')[-1]
            title = response.meta['title']+".PDF"
            self.logger.info('Saving PDF %s', title)
            with open(title, 'wb') as f:
                f.write(response.body)
        except Exception as e:
            print(e)