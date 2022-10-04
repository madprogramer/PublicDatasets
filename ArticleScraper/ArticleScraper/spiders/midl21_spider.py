import scrapy


class QuotesSpider(scrapy.Spider):
    name = "MIDL21_Proceedings"

    def start_requests(self):
        urls = [
            'https://proceedings.mlr.press/v143/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')