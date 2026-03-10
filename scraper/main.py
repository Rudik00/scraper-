from .run_browser import run
from .preservation import save_products


def main():
    url = "https://www.wildberries.ge/catalog/obuv/muzhskaya/kedy-i-krossovki"
    products = run(url=url, scrolls=1)
    save_products(products)


if __name__ == "__main__":
    main()
