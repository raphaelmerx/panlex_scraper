# PanLex scraper
Scrape bilingual vocabulary data from [vocab.panlex.org](https://vocab.panlex.org/)

## Usage

#### 1. Clone this repo: `git clone https://github.com/raphaelmerx/panlex_scraper`

#### 2. Install requirements: `pip install -r requirements.txt`

#### 3. Run the scraping command:

```
scrapy crawl panlex -O panlex.jl -L INFO -a lang1={lang1} -a lang2={lang2}
```

Replacing {lang1} and {lang2} with the 3-letter [ISO 639-2](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes) code of the two languages you want to get parallel vocabulary for.

For example to get Igbo (igo) and English (eng) bitext vocabulary:
```
scrapy crawl panlex -O panlex.jl -L INFO -a lang1=igo -a lang2=eng
```

The scraped data will be in `panlex.jl`, with one json line per vocabulary bitext, e.g.:
```
{"ibo": "\u00e0", "eng": "this"}
{"ibo": "a\u00e0", "eng": "oh"}
{"ibo": "a\u0101", "eng": "oh"}
{"ibo": "\u00e0a", "eng": ""}
{"ibo": "Aba", "eng": "Aba"}
{"ibo": "\u00e0ba", "eng": "flatness"}
{"ibo": "\u00e0b\u00e0ch\u00e0", "eng": "cassava"}
{"ibo": "\u00e0b\u00e0da", "eng": ""}
{"ibo": "abadaba", "eng": "breadth"}
{"ibo": "Abakaliki", "eng": "Abakaliki"}
{"ibo": "\u00e0bal\u00e0", "eng": "fruit of iroko"}
{"ibo": "\u00e0bal\u00e0 \u1ecdj\u1ecb\u0300", "eng": "fruit of iroko"}
{"ibo": "abali", "eng": "night"}
{"ibo": "abal\u00ef", "eng": "night"}
...
```
