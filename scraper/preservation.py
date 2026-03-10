import csv
import os
from dataclasses import asdict
from .models import Product


def save_products(
    products: list[Product],
    output_csv_path: str | None = None,
) -> None:
    # убираем дубликаты по id товара
    unique = []
    seen = set()
    for p in products:
        key = (p.id)
        if key not in seen:
            seen.add(key)
            unique.append(p)

    if output_csv_path is None:
        repo_root = os.path.dirname(os.path.dirname(__file__))
        output_csv_path = os.path.join(repo_root, "data", "products.csv")

    os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
    with open(output_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "price", "img"])
        writer.writeheader()
        for p in unique:
            writer.writerow(asdict(p))

    print(f"Сохранено {len(unique)} уникальных товаров в {output_csv_path}")
