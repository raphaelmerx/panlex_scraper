import scrapy

from ..utils import get_text_from_element



class PanlexIgboScraper(scrapy.Spider):
    name = 'panlex'
    allowed_domains = ['vocab.panlex.org']

    def start_requests(self):
        self.start_url = f'https://vocab.panlex.org/{self.lang1}-000/{self.lang2}-000'
        yield scrapy.Request(url=self.start_url, callback=self.parse)

    def extract_cell_text(self, cell):
        if cell.css('summary'):
            return get_text_from_element(cell.css('summary'))
        return get_text_from_element(cell)

    def parse(self, response):
        """ Parsing of a page. """

        rows = response.css('table tbody tr')
        for row in rows:
            cells = row.css('td')
            yield {
                self.lang1: self.extract_cell_text(cells[0]),
                self.lang2: self.extract_cell_text(cells[1])
            }

        next_button = response.css('main nav .pagination-next')
        if next_button:
            url = self.start_url + next_button.css('::attr(href)').getall()[0]
            yield scrapy.Request(url=url, callback=self.parse)
