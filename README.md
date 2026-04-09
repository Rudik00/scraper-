# WB Product Scraper

A small Python project for scraping product cards from a Wildberries catalog page and saving results to CSV.

Current behavior:
- opens a catalog page in Playwright;
- scrolls the page a specified number of times;
- extracts id, brand (name), price, and image link;
- removes duplicates by id;
- saves output to `data/products.csv`.

## Tech Stack

- Python 3.10+
- Playwright (browser automation)
- BeautifulSoup4 (HTML parsing)

## Project Structure

```
scraper/
	main.py           # entry point
	run_browser.py    # browser launch, scrolling, HTML retrieval
	parser.py         # data extraction from HTML
	models.py         # Product model
	preservation.py   # deduplication and CSV writing
data/
	products.csv      # scraping result
```

## Installation

1. Go to the project folder.
2. Create and activate a virtual environment.
3. Install dependencies.
4. Install a browser for Playwright.

Example for macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
pip install playwright beautifulsoup4
playwright install chromium
```

## Run

Run from the project root as a module:

```bash
python -m scraper.main
```

After execution, the output file will be available at `data/products.csv`.

## Parsed Fields

Each product card includes the following fields:
- `id`
- `name` (brand)
- `price`
- `img` (image URL)

## URL and Scroll Configuration

By default, URL and number of scrolls are set in `scraper/main.py`:

```python
url = "https://www.wildberries.ge/catalog/obuv/muzhskaya/kedy-i-krossovki"
products = run(url=url, scrolls=1)
```

You can change `url` and `scrolls` as needed.

## Notes and Limitations

- Website markup can change, so selectors in `parser.py` may need updates.
- With `headless=True`, the browser runs without UI. For debugging, you can temporarily set `headless=False` in `run_browser.py`.
- Deduplication is done by `id`; if a product has no `id`, it may be treated as a separate record.
