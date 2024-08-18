import scrapy

from ..utils import get_text_from_element



class PanlexIgboScraper(scrapy.Spider):
    name = 'panlex'
    allowed_domains = ['vocab.panlex.org']

    def start_requests(self):
        self.start_url = f'https://vocab.panlex.org/{self.lang1}-000/{self.lang2}-000'
        yield scrapy.Request(url=self.start_url, callback=self.parse_first_page)

    def parse_first_page(self, response):
        """ Parsing of the first page.

        Will find the last page number and yield requests for all pages.
        """
        yield from self.parse_page(response)

        last_page_number = response.css('main nav .pagination-list li')[-1].css('.pagination-link::text').get()
        last_page_number = int(last_page_number)
        for i in range(2, last_page_number + 1):
            url = self.start_url + f'?page={i}'
            yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        """ Parsing of a page. """

        rows = response.css('table tbody tr')
        for row in rows:
            cells = row.css('td')
            yield {
                self.lang1: self.extract_cell_text(cells[0]),
                self.lang2: self.extract_cell_text(cells[1])
            }

    def extract_cell_text(self, cell):
        if cell.css('summary'):
            return get_text_from_element(cell.css('summary'))
        return get_text_from_element(cell)